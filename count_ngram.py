
import numpy as np
import argparse
import pickle


def count_ngram(n, c_path, s_path):
    for i in range(1, n+1):
        print("{}-gram counting".format(i))
        ngram_dict = {}
        path = c_path
        f = open(path, 'r')
        txt1 = f.read()
        txt = txt1.splitlines()
        c_length = len(txt1)
        print('corpus size：', c_length)
        for m, sen in enumerate(txt[:]):
            for index in range(0, len(sen)-n+1):
                if c_length - index >= i:
                    ngram = sen[index:index+i]
                    if ngram not in ngram_dict:
                        ngram_dict[ngram] = 1
                    else:
                        ngram_dict[ngram] += 1
                index += 1
                if index % 10 == 0:
                    print("\r"+str(round(100*(index/c_length), 2))+"%", end=" ")
        ngram_dict1 = {k: v for k, v in ngram_dict.items() if v > 1}
        sort_ngram_dict = sorted(ngram_dict1.items(), key=lambda x: int(x[1]), reverse=True)
        ngram_dict2 = {}
        for data in sort_ngram_dict:
            ngram_dict2[data[0]] = data[1]
        f = open(s_path+str(i)+".pkl", 'wb')
        pickle.dump(ngram_dict2, f)
        f.close()
        f = open(s_path+str(i)+".txt", "w")
        for k, v in ngram_dict2.items():
            f.write(k+','+str(v)+'\n')
        f.close()
        print("\n{}-gram count complete".format(i))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ngram count')
    parser.add_argument('--max-ngram-size', type=int, default=6)
    parser.add_argument('--corpus-path', type=str, default="/home/zyf/桌面/PFNE/data/corpus_wash.txt")
    parser.add_argument('--ngram-path', type=str, default="/home/zyf/桌面/PFNE/ngram")
    config = parser.parse_args()
    # print(config.__dict__)

    count_ngram(config.max_ngram_size, config.corpus_path, config.ngram_path)




