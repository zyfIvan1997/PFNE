#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <locale>
#include <codecvt>
#include <memory>
#include <cmath>
#include <cstdlib>
#include <cstdint>
#include <cassert>
#include <algorithm>
#include <unordered_map>
#include <numeric>
#include <thread>
#include <mutex>
#include "docopt.cpp/docopt.h"

#define SIZE_TABLE_UNIGRAM 1000000
#define SIZE_CHUNK_PROGRESSBAR 1000

typedef double real_t;

const std::codecvt_mode kBom = static_cast<std::codecvt_mode>(std::generate_header | std::consume_header);
typedef std::codecvt_utf8<wchar_t, 0x10ffff, kBom> WideConvUtf8Bom;
static const char USAGE[] =
R"(w2v-sembei: Segmentation-free version of word2vec

Usage:
    ./w2v-sembei --corpus=<corpus> --dim=<dim> --window=<window> --ng=<ng> --ng_count=<ng_count> [--output=<output> --seed=<seed> --rate=<rate> --n_iter=<n_iter> --negative=<negative>  --sample=<sample> --cores=<cores> --debug]

Options:
    -h --help             Show this screen.
    -v --version          Show version.
    --corpus=<corpus>     File path of text file (without newline)
    --output=<output>     Output directory  [default: ./output/]
    --dim=<dim>           Dimension of vector representation
    --window=<window>     (currently unavailable) Size of context window
    --ng=<ng>             File path of ngram
    --ng_count=<ng_count> File path of ngram_count
    --cores=<cores>       Number of cores to use [default: 1]
    --seed=<seed>         Random seed for CheapRand [default: 123]
    --rate=<rate>         Initial learning rate [default: 0.1]
    --n_iter=<n_iter>     Number of iteration [default: 5]
    --negative=<negative> Number of negative samples  [default: 10]
    --sample=<sample>     Rate for negative sampling  [default: 0.0001]
    --debug               Debug option [default: false]
)";

class CheapRand {
private:
  uint64_t randomstate;

public:
  CheapRand() {
    randomstate = 0;
  }

  explicit CheapRand(int64_t _seed) {
    assert(_seed >= 0);
    randomstate = _seed;
  }

  CheapRand(CheapRand& cheaprand) {
    randomstate = cheaprand.get_randomstate();
  }

  int64_t get_randomstate() { return randomstate; }

  inline int64_t generate_randint(const int64_t max) {
    assert(max > 0);
    randomstate = randomstate * 25214903917 + 11;
    return std::abs(static_cast<int64_t>(randomstate >> 16)) % max;
  }

  inline real_t generate_rand_uniform(const real_t _min, const real_t _max) {
    return _min + (_max - _min) * generate_randint(65536) / static_cast<real_t>(65536);
  }
};


class PFNE {
private:
  const std::wstring corpus;
  const std::vector<std::wstring> vocabulary;
  const std::vector<int64_t> count_vocabulary;
  const int64_t size_window;
  const int64_t dim_embedding;
  const bool verbose;
  const int64_t seed;
  const real_t learning_rate;
  const int64_t n_iteration;
  const int64_t n_negative_sample;
  const real_t rate_sample;
  const real_t power_unigram_table;

  int64_t size_vocabulary;
  int64_t sum_count_vocabulary;
  int64_t max_length_word;
  std::unordered_map<std::wstring, int64_t> vocabulary2id;

  CheapRand cheaprand;
  int64_t* table_unigram;
  real_t* embeddings_words;
  real_t* embeddings_contexts_left;
  real_t* embeddings_contexts_right;

public:
  PFNE(const std::wstring& _corpus,
                 const std::vector<std::wstring>& _vocabulary,
                 const std::vector<int64_t>& _count_vocabulary,
                 const int64_t _size_window,
                 const int64_t _dim_embedding,
                 const bool _verbose,
                 const int64_t _seed,
                 const real_t _learning_rate,
                 const int64_t _n_iteration,
                 const int64_t _n_negative_sample,
                 const real_t _rate_sample,
                 const real_t _power_unigram_table);
  ~PFNE();
  void train_model(const int64_t n_cores);
  void to_csv(const std::string output_prefix);
  void print_settings();

private:
  void train_model_eachthread(const int64_t id_thread,
                              const int64_t i_wstr_start,
                              const int64_t length_str,
                              const int64_t n_cores);
  void initialize_parameters();
  void construct_unigramtable(const real_t power_unigram_table);
};

PFNE::PFNE(const std::wstring& _corpus,
                               const std::vector<std::wstring>& _vocabulary,
                               const std::vector<int64_t>& _count_vocabulary,
                               const int64_t _size_window,
                               const int64_t _dim_embedding,
                               const bool _verbose,
                               const int64_t _seed,
                               const real_t _learning_rate,
                               const int64_t _n_iteration,
                               const int64_t _n_negative_sample,
                               const real_t _rate_sample,
                               const real_t _power_unigram_table)
  : corpus(_corpus),
    vocabulary(_vocabulary),
    count_vocabulary(_count_vocabulary),
    size_window(_size_window),
    dim_embedding(_dim_embedding),
    verbose(_verbose),
    seed(_seed),
    learning_rate(_learning_rate),
    n_iteration(_n_iteration),
    n_negative_sample(_n_negative_sample),
    rate_sample(_rate_sample),
    power_unigram_table(_power_unigram_table)
{
  assert(size_window >= 0);
  assert(dim_embedding > 0);
  assert(seed > 0);
  assert(n_iteration >= 0);
  assert(learning_rate > 0);
  assert(n_negative_sample >= 0);
  assert(rate_sample > 0);
  assert(power_unigram_table > 0);

  size_vocabulary = vocabulary.size();
  sum_count_vocabulary = std::accumulate(count_vocabulary.begin(), count_vocabulary.end(), 0);
  max_length_word = 0;
  for (auto &v : vocabulary) {
    const int64_t length = v.size();
    if (length > max_length_word) max_length_word = length;
  }

  cheaprand = CheapRand(seed);

  for (int64_t i=0; i<size_vocabulary; i++) {
    vocabulary2id[vocabulary[i]] = i;
  }

  initialize_parameters();
  construct_unigramtable(power_unigram_table);

  if (verbose) print_settings();
}

void PFNE::print_settings() {
  std::wcout << std::endl;
  std::wcout << "===== PFNE =====" << std::endl;
  std::wcout << "corpus.size()       : " << corpus.size() << std::endl;
  std::wcout << "vocabulary.size() : " << vocabulary.size() << std::endl;
  std::wcout << "size_window       : " << size_window << std::endl;
  std::wcout << "dim_embedding     : " << dim_embedding << std::endl;
  std::wcout << "seed              : " << seed << std::endl;
  std::wcout << "learning_rate     : " << learning_rate << std::endl;
  std::wcout << "n_iteration       : " << n_iteration << std::endl;
  std::wcout << "max_length_word   : " << max_length_word << std::endl;
  std::wcout << "n_negative_sample : " << n_negative_sample << std::endl;
  std::wcout << "rate_sample       : " << rate_sample << std::endl;
  std::wcout << "==========================" << std::endl;
}

PFNE::~PFNE() {
  delete[] embeddings_words;
  delete[] embeddings_contexts_left;
  delete[] embeddings_contexts_right;
  delete[] table_unigram;
}

void PFNE::initialize_parameters() {
  const int64_t n = size_vocabulary*dim_embedding;
  const real_t _min = -1.0/dim_embedding;
  const real_t _max =  1.0/dim_embedding;

  // Allocates memory for vector representations
  embeddings_words          = new real_t[n];
  embeddings_contexts_left  = new real_t[n];
  embeddings_contexts_right = new real_t[n];

  for (int64_t i=0; i<n; i++) {
    embeddings_words[i] = cheaprand.generate_rand_uniform(_min, _max);
    embeddings_contexts_left[i] = 0.0;
    embeddings_contexts_right[i] = 0.0;
  }
}

void PFNE::train_model(const int64_t n_cores) {
  const int64_t length_wstr = corpus.size();
  const int64_t length_chunk = length_wstr / n_cores;
  int64_t i_wstr_start = 0;
  std::vector<std::thread> vector_threads(n_cores);

  for (int64_t id_thread=0; id_thread<n_cores; id_thread++) {
    vector_threads.at(id_thread) = std::thread(&PFNE::train_model_eachthread,
                                               this,
                                               id_thread,
                                               i_wstr_start, length_chunk, n_cores);
    i_wstr_start += length_chunk;
  }

  for (int64_t id_thread=0; id_thread<n_cores; id_thread++) {
    vector_threads.at(id_thread).join();
  }
}

void PFNE::train_model_eachthread(const int64_t id_thread,
                                            const int64_t i_wstr_start,
                                            const int64_t length_str,
                                            const int64_t n_cores) {
  const std::wstring wstr_thread = corpus.substr(i_wstr_start, length_str);
  std::unordered_map<std::wstring, int64_t> vocabulary2id_thread = vocabulary2id;
  std::vector<int64_t> count_vocabulary_thread = count_vocabulary;

  real_t* gradient_words = new real_t[dim_embedding];
  CheapRand cheaprand_thread(id_thread + seed);

  if (id_thread == 0) std::wcout << std::endl;

  for (int64_t i_iteration=0; i_iteration<n_iteration; i_iteration++) {
    // For each position in corpus
    for (int64_t i_str=0; i_str<length_str; i_str++) {

      if (id_thread == n_cores - 1) {
        const int64_t i_progress = i_iteration * length_str + i_str;
        if (i_progress % SIZE_CHUNK_PROGRESSBAR == 0) {
          // Print progress
          const double percent = 100 * (double)i_progress / (n_iteration * length_str);
          std::wcout << "\rProgress : "
                     << std::fixed << std::setprecision(2) << percent
                     << "%     " << std::flush;

          // TODO: Output loss

        }
      }

      real_t ratio_completed = (i_iteration*length_str + i_str) / static_cast<real_t>(n_iteration*length_str + 1);
      if (ratio_completed > 0.9999) ratio_completed = 0.9999;
      const real_t _learning_rate = learning_rate * (1 - ratio_completed);

      // For each (center) word
      for (int64_t length_word=1; length_word<=max_length_word; length_word++) {
        if (i_str + length_word - 1 >= length_str) break;

        const std::wstring word = wstr_thread.substr(i_str, length_word);
        if (vocabulary2id_thread.find(word) == vocabulary2id_thread.end()) continue;  // continue if `word` is not in vocabulary
        const int64_t id_word = vocabulary2id_thread[word];

        const int64_t freq = count_vocabulary_thread[id_word];
        const real_t probability_reject = (sqrt(freq/(rate_sample*sum_count_vocabulary)) + 1) * (rate_sample*sum_count_vocabulary) / freq;
        if (probability_reject < cheaprand_thread.generate_rand_uniform(0, 1)) continue;

        // For each context word
        for (int64_t length_context=1; length_context<=max_length_word; length_context++) {
          if (i_str + length_word + length_context - 1 >= length_str) break;

          const std::wstring context = wstr_thread.substr(i_str + length_word, length_context);
          if (vocabulary2id_thread.find(context) == vocabulary2id_thread.end()) continue;  // continue if `context` is not in vocabulary
          const int64_t id_context = vocabulary2id_thread[context];


          //// Skip-gram with negative sampling

          // Vector representation of `word` can be obtained by
          //  (embeddings_words[i_head_word], ..., embeddings_words[i_head_word + dim_embedding - 1]).
          int64_t i_head_word, i_head_context, i_head_target;

          for (const bool is_right_context : {true, false}) {
            if (is_right_context) { // Right context
              i_head_word = dim_embedding * id_word;
              i_head_context = dim_embedding * id_context;
            } else { // Left context
              i_head_word = dim_embedding * id_context;
              i_head_context = dim_embedding * id_word;
            }

            for (int64_t i=0; i<dim_embedding; i++) {
              gradient_words[i] = 0;
            }

            for (int64_t i_ns=-1; i_ns<n_negative_sample; i_ns++) {
              const bool is_negative_sample = (i_ns >= 0);

              if (is_negative_sample) {
                i_head_target = dim_embedding * table_unigram[cheaprand_thread.generate_randint(SIZE_TABLE_UNIGRAM)];
                if (i_head_target == i_head_context) {
                  continue;
                }
              } else {
                i_head_target = i_head_context;
              }

              real_t x = 0;
              for (int64_t i=0; i<dim_embedding; i++) {
                if (is_right_context) {
                  x += embeddings_words[i_head_word + i] * embeddings_contexts_right[i_head_target + i];
                } else {
                  x += embeddings_words[i_head_word + i] * embeddings_contexts_left[i_head_target + i];
                }
              }

              const real_t g = 1. / (1. + exp(-x)) - (1.0 - (real_t)is_negative_sample);

              for (int64_t i=0; i<dim_embedding; i++) {
                if (is_right_context) {
                  gradient_words[i] += g * embeddings_contexts_right[i_head_target + i];
                  embeddings_contexts_right[i_head_target + i] -= _learning_rate * g * embeddings_words[i_head_word + i];
                } else {
                  gradient_words[i] += g * embeddings_contexts_left[i_head_target + i];
                  embeddings_contexts_left[i_head_target + i] -= _learning_rate * g * embeddings_words[i_head_word + i];
                }
              }
            }

            for (int64_t i=0; i<dim_embedding; i++) {
              embeddings_words[i_head_word + i] -= _learning_rate * gradient_words[i];
            }
          }
        }
      }
    }
  }

  delete[] gradient_words;
  if (id_thread == 0) std::wcout << std::endl << std::flush;
}

void PFNE::construct_unigramtable(const real_t power_unigram_table) {
  table_unigram = new int64_t[SIZE_TABLE_UNIGRAM];
  real_t sum_count_power = 0;

  for (auto c : count_vocabulary) {
    sum_count_power += pow(c, power_unigram_table);
  }

  int64_t id_word = 0;
  real_t cumsum_count_power = pow(count_vocabulary[id_word], power_unigram_table)/sum_count_power;

  for (int64_t i_table=0; i_table<SIZE_TABLE_UNIGRAM; i_table++) {
    table_unigram[i_table] = id_word;
    if (i_table / static_cast<real_t>(SIZE_TABLE_UNIGRAM) > cumsum_count_power) {
      id_word++;
      cumsum_count_power += pow(count_vocabulary[id_word], power_unigram_table)/sum_count_power;
    }
    if (id_word >= size_vocabulary) id_word = size_vocabulary - 1;
  }
}

void PFNE::to_csv(const std::string output_prefix) {

  std::wofstream ofs;
  WideConvUtf8Bom cvt(1);
  std::locale loc(ofs.getloc(), &cvt);
  ofs.imbue(std::locale(std::locale(), new std::codecvt_utf8<wchar_t>));

  // Output vocabulary words
  ofs.open(output_prefix + "/vocabulary.csv", std::ios::out | std::ios_base::trunc);
  for (auto v : vocabulary) {
    ofs << v << std::endl;
  }
  ofs.close();

  // Output vector representation of words
  ofs.open(output_prefix + "/embeddings_words.csv", std::ios::out | std::ios_base::trunc);
  for (int64_t i_vocabulary=0; i_vocabulary<size_vocabulary; i_vocabulary++) {
    for (int64_t i_dim=0; i_dim<dim_embedding; i_dim++) {
      ofs << embeddings_words[i_vocabulary*dim_embedding + i_dim];
      if (i_dim < dim_embedding - 1) ofs << " ";
    }
    ofs << std::endl << std::flush; // FIXME:endl 内で flush してるらしいので要らないかも
  }
  ofs.close();
}

std::wstring UTF8ToWString(const std::string& str) 
{
    std::wstring_convert<std::codecvt_utf8<wchar_t>> converter;
    std::wstring wide_string = converter.from_bytes(str);
    return wide_string;
}

void loadFile(const std::string& file, std::vector<std::wstring>& ngram_input) {
  std::ifstream input;
  if (!input.is_open()) {
    input.open(file, std::ios::in);
    std::string line;
    while (std::getline(input, line)) {
      ngram_input.push_back(UTF8ToWString(line));
    }
  }
}

void loadFile_count(const std::string& file, std::vector<std::string>& ngram_count_input) {
  std::ifstream input;
  if (!input.is_open()) {
    input.open(file, std::ios::in);
    std::string line;
    while (std::getline(input, line)) {
      ngram_count_input.push_back(line);
    }
  }
}



int main(int argc, const char** argv) {
  // Parse command line arguments
  std::map<std::string, docopt::value> args
    = docopt::docopt(USAGE, { argv + 1, argv + argc }, true, "w2v-sembei v0.1");
  const std::string path_corpus     = args["--corpus"  ].asString();
  const std::string dir_output      = args["--output"  ].asString();
  const std::string ng_path         = args["--ng"      ].asString();
  const std::string ng_count_path   = args["--ng_count"].asString();
  const int64_t     size_window     = args["--window"  ].asLong();
  const int64_t     dim_embedding   = args["--dim"     ].asLong();
  const int64_t     seed            = args["--seed"    ].asLong();
  const bool        debug           = args["--debug"   ].asBool();
  const int64_t     n_iteration     = args["--n_iter"  ].asLong();
  const int64_t     n_negative      = args["--negative"].asLong();
  const int64_t     n_cores         = args["--cores"   ].asLong();
  const real_t learning_rate                   = static_cast<real_t>(std::stod(args["--rate"   ].asString()));
  const real_t rate_sample                     = static_cast<real_t>(std::stod(args["--sample" ].asString()));
  // const real_t epsilon_lossycounting           = static_cast<real_t>(std::stod(args["--epsilon"].asString()));
  // const real_t support_threshold_lossycounting = static_cast<real_t>(std::stod(args["--support"].asString()));
  // const std::vector<std::string> size_vocabulary_str_list = args["<vocab>"].asStringList();
  const real_t power_unigram_table = 0.75;


  // Settings for std::wcout
  std::setlocale(LC_CTYPE, "");

  std::wifstream file;
  WideConvUtf8Bom cvt(1);
  std::locale loc(file.getloc(), &cvt);
  auto locale_old = file.imbue(loc);
  file.open(path_corpus, std::ios::in | std::ios::binary);

  std::wstringstream wss;
  wss << file.rdbuf();
  std::wstring ws = wss.str();
  file.close();
  file.imbue(locale_old);

////////////////////////////////////////////////////////////////////
  std::wcout << "  Load N-grams & Counts " << std::endl;
  std::cout << "ng_path: " << ng_path << std::endl;
  std::cout << "ng_count_path:  " << ng_count_path << std::endl;
  
  // Load N-gram & Counts
  std::vector<std::wstring> ngram_input;
  loadFile(ng_path, ngram_input);
  std::wcout << "ngram_input.size(): " << ngram_input.size() << std::endl;

  std::vector<std::string> ngram_count_input;
  loadFile_count(ng_count_path, ngram_count_input);
  std::wcout << "ngram_count_input.size(): " << ngram_count_input.size() << std::endl;

  // WString - to - Int
  std::wcout << "  Counts -- WString-to-Int " << std::endl;
  std::vector<std::int64_t> ngram_count_int_input;
  for (auto& v : ngram_count_input) {
    ngram_count_int_input.push_back(std::atoi(v.c_str()));
  }
  std::wcout << "ngram_count_int_input.size(): " << ngram_count_int_input.size() << std::endl;

  // // print 
  std::wcout << " print first 5 elems "<< std::endl;
  for (int64_t i = 0; i < 5; i++) {
    std::wcout << "++++++++++ "<< std::endl;
    std::wcout << ngram_count_int_input[i] << std::endl;
    std::wcout << ngram_input[i] << std::endl;
  }

/////////////////////////////////////////////////////////////////////////////////////


  // Extract frequently-used n-grams using lossy counting algorithm
//   std::vector<std::wstring> vocabulary;
//   std::vector<int64_t> count_vocabulary;

// std::vector<int64_t> size_vocabulary_list;

//   for (auto& s : size_vocabulary_str_list) {
//     size_vocabulary_list.push_back(std::stoi(s));
//   }

//   LossyCountingNgram lcn(ws, size_vocabulary_list, n_cores,
//                          epsilon_lossycounting, support_threshold_lossycounting, debug);
//   lcn.extract_ngram();
//   lcn.to_csv(dir_output);
//   lcn.get_ngram_frequency(vocabulary, count_vocabulary);

  // Word embedding using PFNE
  PFNE w2vsb(ws, ngram_input, ngram_count_int_input,
                       size_window, dim_embedding, debug, seed,
                       learning_rate, n_iteration, n_negative,
                       rate_sample, power_unigram_table);
  w2vsb.train_model(n_cores);
  w2vsb.to_csv(dir_output);

  return 0;
}
