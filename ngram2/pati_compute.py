
import pickle
import numpy as np
import argparse
import pickle


def access_sum(t_path, s_path):
    access_a_f = {}
    access_b_b = {}
    sum_a = {}
    sum_b = {}
    v_1 = {}
    f1 = open(s_path + "access_a.pkl", "wb")
    f2 = open(s_path + "access_b.pkl", "wb")
    f9 = open(s_path + "sum_a.pkl", "wb")
    f10 = open(s_path + "sum_b.pkl", "wb")
    f17 = open(s_path + "v_1.pkl", "wb")
    ii = 0
    ff = open(t_path, "r")
    for line in ff:
        key = line.split(',')[0]
        val = int(line.split(',')[1])
        k_1 = key[0:1]
        k_2 = key[1:2]
        if k_1 not in access_a_f:
            access_a_f[k_1] = 1
            sum_a[k_1] = val
        else:
            access_a_f[k_1] += 1
            sum_a[k_1] += val
        if k_2 not in access_b_b:
            access_b_b[k_2] = 1
            sum_b[k_2] = val
        else:
            access_b_b[k_2] += 1
            sum_b[k_2] += val
        if k_1 not in v_1:
            v_1[k_1] = val
        else:
            v_1[k_1] += val
        if k_2 not in v_1:
            v_1[k_2] = val
        else:
            v_1[k_2] += val

    pickle.dump(access_a_f, f1)
    pickle.dump(access_b_b, f2)
    pickle.dump(sum_a, f9)
    pickle.dump(sum_b, f10)
    pickle.dump(v_1, f17)
    ff.close()
    f1.close()
    f2.close()
    f9.close()
    f10.close()
    f17.close()


def mp_at_f(p_path, c_path, l_path):
    f = open(p_path, "rb")
    ngram_4 = pickle.load(f)
    s_n = len(ngram_4)
    f = open(c_path, "r")
    total_word = len(f.read())
    print(total_word)
    f1 = open(l_path+"access_a.pkl", "rb")
    f2 = open(l_path+"access_b.pkl", "rb")
    f7 = open(l_path+"sum_a.pkl", "rb")
    f8 = open(l_path+"sum_b.pkl", "rb")
    f13 = open(l_path+"v_1.pkl", "rb")
    access_a_f = pickle.load(f1)
    access_b_b = pickle.load(f2)
    value_a_f = pickle.load(f7)
    value_b_b = pickle.load(f8)
    v_1 = pickle.load(f13)
    m_t_f = {}
    mmm = 0
    error = 0
    for key, val in ngram_4.items():
        try:
            improve = []
            times = []

            key_0 = key[0:1]
            key_1 = key[1:2]
            improve1 = np.power(ngram_4[key] / (v_1[key_0] + v_1[key_1]), 2) / (
                        (v_1[key_0] / total_word) * (v_1[key_1] / total_word))
            r1 = ngram_4[key] / value_a_f[key_0]
            r2 = ngram_4[key] / value_b_b[key_1]
            if r1 >= r2:
                times1 = r1 / (1 / access_a_f[key_0])
            else:
                times1 = r2 / (1 / access_b_b[key_1])
            improve.append(improve1)
            times.append(times1)

            min_improve = min(improve)
            index_min = improve.index(min(improve))
            improve_times = times[index_min]
            mmm += 1
            if mmm % 10 == 0:
                print("\r"+str(round(100*(mmm/s_n), 2))+"%", end=" ")

            m_t_f[key] = (key, ngram_4[key], min_improve, improve_times)
        except KeyError:
            pass
            error += 1
    print("keyerror:", error)
    dump_path = l_path+"edge.pkl"
    f = open(dump_path, "wb")
    pickle.dump(m_t_f, f)
    print("存储完成")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=' count')
    parser.add_argument('--corpus-path', type=str, default="/home/zyf/桌面/PFNE/data/corpus_wash.txt")
    parser.add_argument('--ngram-txt', type=str, default="/home/zyf/桌面/PFNE/ngram2.txt")
    parser.add_argument('--ngram-pkl', type=str, default="/home/zyf/桌面/PFNE/ngram2.pkl")
    parser.add_argument('--access-sum-path', type=str, default="/home/zyf/桌面/PFNE/ngram2/")
    parser.add_argument('--min-count', type=int, default=1)
    parser.add_argument('--ngram-word', type=str, default="/home/zyf/桌面/PFNE/embedding/ngram_word.txt")
    parser.add_argument('--ngram-count', type=str, default="/home/zyf/桌面/PFNE/embedding/ngram_count.txt")
    config = parser.parse_args()

    access_sum(config.ngram_txt, config.access_sum_path)

    mp_at_f(config.ngram_pkl, config.corpus_path, config.access_sum_path)

    load_path = config.access_sum_path+"edge.pkl"
    f = open(load_path, "rb")
    all_info = pickle.load(f)
    print(len(all_info))
    word = [key for key, val in all_info.items()]
    mp = [val[2] for key, val in all_info.items()]
    fre = [val[1] for key, val in all_info.items()]
    times = [val[3] for key, val in all_info.items()]
    pati = [(word[i], mp[i] * (1 + float(np.abs(np.math.log(times[i], 10)))) * fre[i], fre[i]) for i in range(len(all_info))]
    pati_sort = sorted(pati, key=lambda item: item[1], reverse=True)
    pati_sort = [data for data in pati_sort if '的' not in data[0]]
    pati_sort = [data for data in pati_sort if '是' not in data[0]]
    dump_path = config.access_sum_path+"pati_sort.pkl"
    f = open(dump_path, "wb")
    pickle.dump(pati_sort, f)
    f.close()
    ff_w = open(config.ngram_word, 'a')
    ff_c = open(config.ngram_count, 'a')
    for m, data in enumerate(pati_sort):
        if data[2] > config.min_count:
            ff_w.write(data[0] + '\n')
            ff_c.write(str(data[2]) + '\n')
            if m == config.voca_size:
                break
    ff_w.close()
    ff_c.close()












