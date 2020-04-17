
import pickle
import numpy as np
import argparse
import pickle


def access_sum(t_path, s_path):
    access_a_f = {}
    access_bc_b = {}
    access_ab_f = {}
    access_c_b = {}
    sum_a = {}
    sum_bc = {}
    sum_ab = {}
    sum_c = {}
    v_1 = {}
    v_2 = {}
    f1 = open(s_path + "access_a.pkl", "wb")
    f2 = open(s_path + "access_bc.pkl", "wb")
    f3 = open(s_path + "access_ab.pkl", "wb")
    f4 = open(s_path + "access_c.pkl", "wb")
    f9 = open(s_path + "sum_a.pkl", "wb")
    f10 = open(s_path + "sum_bc.pkl", "wb")
    f11 = open(s_path + "sum_ab.pkl", "wb")
    f12 = open(s_path + "sum_c.pkl", "wb")
    f17 = open(s_path + "v_1.pkl", "wb")
    f18 = open(s_path + "v_2.pkl", "wb")
    ff = open(t_path, "r")
    for line in ff:
        key = line.split(',')[0]
        val = int(line.split(',')[1])
        k_1 = key[0:1]
        k_23 = key[1:3]
        k_12 = key[0:2]
        k_3 = key[2:3]
        if k_1 not in access_a_f:
            access_a_f[k_1] = 1
            sum_a[k_1] = val
        else:
            access_a_f[k_1] += 1
            sum_a[k_1] += val
        # info_a.setdefault(k_1, []).append((key, ngram_5[key]))
        if k_23 not in access_bc_b:
            access_bc_b[k_23] = 1
            sum_bc[k_23] = val
        else:
            access_bc_b[k_23] += 1
            sum_bc[k_23] += val
        if k_12 not in access_ab_f:
            access_ab_f[k_12] = 1
            sum_ab[k_12] = val
        else:
            access_ab_f[k_12] += 1
            sum_ab[k_12] += val
        if k_3 not in access_c_b:
            access_c_b[k_3] = 1
            sum_c[k_3] = val
        else:
            access_c_b[k_3] += 1
            sum_c[k_3] += val
        if k_1 not in v_1:
            v_1[k_1] = val
        else:
            v_1[k_1] += val
        if k_23 not in v_2:
            v_2[k_23] = val
        else:
            v_2[k_23] += val

        if k_12 not in v_2:
            v_2[k_12] = val
        else:
            v_2[k_12] += val
        if k_3 not in v_1:
            v_1[k_3] = val
        else:
            v_1[k_3] += val
    pickle.dump(access_a_f, f1)
    pickle.dump(access_bc_b, f2)
    pickle.dump(access_ab_f, f3)
    pickle.dump(access_c_b, f4)
    pickle.dump(sum_a, f9)
    pickle.dump(sum_bc, f10)
    pickle.dump(sum_ab, f11)
    pickle.dump(sum_c, f12)
    pickle.dump(v_1, f17)
    pickle.dump(v_2, f18)
    ff.close()
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f9.close()
    f10.close()
    f11.close()
    f12.close()
    f17.close()
    f18.close()


def mp_at_f(p_path, c_path, l_path):
    f = open(p_path, "rb")
    ngram_4 = pickle.load(f)
    s_n = len(ngram_4)
    f = open(c_path, "r")
    total_word = len(f.read())
    print(total_word)
    f1 = open(l_path+"access_a.pkl", "rb")
    f2 = open(l_path+"access_bc.pkl", "rb")
    f3 = open(l_path+"access_ab.pkl", "rb")
    f4 = open(l_path+"access_c.pkl", "rb")
    f7 = open(l_path+"sum_a.pkl", "rb")
    f8 = open(l_path+"sum_bc.pkl", "rb")
    f9 = open(l_path+"sum_ab.pkl", "rb")
    f10 = open(l_path+"sum_c.pkl", "rb")
    f13 = open(l_path+"v_1.pkl", "rb")
    f14 = open(l_path+"v_2.pkl", "rb")
    access_a_f = pickle.load(f1)
    access_bc_b = pickle.load(f2)
    access_ab_f = pickle.load(f3)
    access_c_b = pickle.load(f4)
    value_a_f = pickle.load(f7)
    value_bc_b = pickle.load(f8)
    value_ab_f = pickle.load(f9)
    value_c_b = pickle.load(f10)
    v_1 = pickle.load(f13)
    v_2 = pickle.load(f14)

    m_t_f = {}
    mmm = 0
    error = 0
    for key, val in ngram_4.items():
        try:
            improve = []
            times = []
            key_0 = key[0:1]
            key_12 = key[1:3]
            improve1 = (np.power(ngram_4[key] / (v_1[key_0] + v_2[key_12]), 2) / (
                        (v_1[key_0] / total_word) * (v_2[key_12] / total_word)))
            r1 = ngram_4[key] / value_a_f[key_0]
            r2 = ngram_4[key] / value_bc_b[key_12]
            if r1 >= r2:
                times1 = r1 / (1 / access_a_f[key_0])
            else:
                times1 = r2 / (1 / access_bc_b[key_12])
            improve.append(improve1)
            times.append(times1)
            key_01 = key[0:2]
            key_2 = key[2:3]
            improve2 = (np.power(ngram_4[key] / (v_2[key_01] + v_1[key_2]), 2) / (
                        (v_2[key_01] / total_word) * (v_1[key_2] / total_word)))
            r3 = ngram_4[key] / value_ab_f[key_01]
            r4 = ngram_4[key] / value_c_b[key_2]
            if r3 >= r4:
                times2 = r3 / (1 / access_ab_f[key_01])
            else:
                times2 = r4 / (1 / access_c_b[key_2])
            improve.append(improve2)
            times.append(times2)
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='pati computation')
    parser.add_argument('--corpus-path', type=str, default="/home/zyf/桌面/PFNE/data/corpus_wash.txt")
    parser.add_argument('--ngram-txt', type=str, default="/home/zyf/桌面/PFNE/ngram3.txt")
    parser.add_argument('--ngram-pkl', type=str, default="/home/zyf/桌面/PFNE/ngram3.pkl")
    parser.add_argument('--access-sum-path', type=str, default="/home/zyf/桌面/PFNE/ngram3/")
    parser.add_argument('--min-count', type=int, default=1)
    parser.add_argument('--ngram-word', type=str, default="/home/zyf/桌面/PFNE/embedding/ngram_word.txt")
    parser.add_argument('--ngram-count', type=str, default="/home/zyf/桌面/PFNE/embedding/ngram_count.txt")
    parser.add_argument('--voca-size', type=int, default=300000)
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












