
import pickle
import numpy as np
import argparse
import pickle


def access_sum(t_path, s_path):
    access_a_f = {}
    access_bcd_b = {}
    access_ab_f = {}
    access_cd_b = {}
    access_abc_f = {}
    access_d_b = {}
    sum_a = {}
    sum_bcd = {}
    sum_ab = {}
    sum_cd = {}
    sum_abc = {}
    sum_d = {}
    v_1 = {}
    v_2 = {}
    v_3 = {}
    f1 = open(s_path+"access_a.pkl", "wb")
    f2 = open(s_path+"access_bcd.pkl", "wb")
    f3 = open(s_path+"access_ab.pkl", "wb")
    f4 = open(s_path+"access_cd.pkl", "wb")
    f5 = open(s_path+"access_abc.pkl", "wb")
    f6 = open(s_path+"access_d.pkl", "wb")
    f9 = open(s_path+"sum_a.pkl", "wb")
    f10 = open(s_path+"sum_bcd.pkl", "wb")
    f11 = open(s_path+"sum_ab.pkl", "wb")
    f12 = open(s_path+"sum_cd.pkl", "wb")
    f13 = open(s_path+"sum_abc.pkl", "wb")
    f14 = open(s_path+"sum_d.pkl", "wb")
    f17 = open(s_path+"v_1.pkl", "wb")
    f18 = open(s_path+"v_2.pkl", "wb")
    f19 = open(s_path+"v_3.pkl", "wb")
    ff = open(t_path, "r")
    for line in ff:
        key = line.split(',')[0]
        val = int(line.split(',')[1])
        k_1 = key[0:1]
        k_234 = key[1:4]
        k_12 = key[0:2]
        k_34 = key[2:4]
        k_123 = key[0:3]
        k_4 = key[3:4]
        if k_1 not in access_a_f:
            access_a_f[k_1] = 1
            sum_a[k_1] = val
        else:
            access_a_f[k_1] += 1
            sum_a[k_1] += val
        if k_234 not in access_bcd_b:
            access_bcd_b[k_234] = 1
            sum_bcd[k_234] = val
        else:
            access_bcd_b[k_234] += 1
            sum_bcd[k_234] += val
        if k_12 not in access_ab_f:
            access_ab_f[k_12] = 1
            sum_ab[k_12] = val
        else:
            access_ab_f[k_12] += 1
            sum_ab[k_12] += val
        if k_34 not in access_cd_b:
            access_cd_b[k_34] = 1
            sum_cd[k_34] = val
        else:
            access_cd_b[k_34] += 1
            sum_cd[k_34] += val
        if k_123 not in access_abc_f:
            access_abc_f[k_123] = 1
            sum_abc[k_123] = val
        else:
            access_abc_f[k_123] += 1
            sum_abc[k_123] += val
        if k_4 not in access_d_b:
            access_d_b[k_4] = 1
            sum_d[k_4] = val
        else:
            access_d_b[k_4] += 1
            sum_d[k_4] += val
        if k_1 not in v_1:
            v_1[k_1] = val
        else:
            v_1[k_1] += val
        if k_234 not in v_3:
            v_3[k_234] = val
        else:
            v_3[k_234] += val
        if k_12 not in v_2:
            v_2[k_12] = val
        else:
            v_2[k_12] += val
        if k_34 not in v_2:
            v_2[k_34] = val
        else:
            v_2[k_34] += val
        if k_123 not in v_3:
            v_3[k_123] = val
        else:
            v_3[k_123] += val
        if k_4 not in v_1:
            v_1[k_4] = val
        else:
            v_1[k_4] += val
    pickle.dump(access_a_f, f1)
    pickle.dump(access_bcd_b, f2)
    pickle.dump(access_ab_f, f3)
    pickle.dump(access_cd_b, f4)
    pickle.dump(access_abc_f, f5)
    pickle.dump(access_d_b, f6)
    pickle.dump(sum_a, f9)
    pickle.dump(sum_bcd, f10)
    pickle.dump(sum_ab, f11)
    pickle.dump(sum_cd, f12)
    pickle.dump(sum_abc, f13)
    pickle.dump(sum_d, f14)
    pickle.dump(v_1, f17)
    pickle.dump(v_2, f18)
    pickle.dump(v_3, f19)
    ff.close()
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f9.close()
    f10.close()
    f11.close()
    f12.close()
    f13.close()
    f14.close()
    f17.close()
    f18.close()
    f19.close()


def mp_at_f(p_path, c_path, l_path):
    f = open(p_path, "rb")
    ngram_4 = pickle.load(f)
    s_n = len(ngram_4)
    f = open(c_path, "r")
    total_word = len(f.read())
    print(total_word)

    f1 = open(l_path+"access_ab.pkl", "rb")
    f2 = open(l_path+"access_cd.pkl", "rb")
    f3 = open(l_path+"access_abc.pkl", "rb")
    f4 = open(l_path+"access_d.pkl", "rb")
    f5 = open(l_path+"access_a.pkl", "rb")
    f6 = open(l_path+"access_bcd.pkl", "rb")
    f7 = open(l_path+"sum_ab.pkl", "rb")
    f8 = open(l_path+"sum_cd.pkl", "rb")
    f9 = open(l_path+"sum_a.pkl", "rb")
    f10 = open(l_path+"sum_bcd.pkl", "rb")
    f11 = open(l_path+"sum_abc.pkl", "rb")
    f12 = open(l_path+"sum_d.pkl", "rb")
    f13 = open(l_path+"v_1.pkl", "rb")
    f14 = open(l_path+"v_2.pkl", "rb")
    f15 = open(l_path+"v_3.pkl", "rb")

    access_ab_f = pickle.load(f1)
    access_cd_b = pickle.load(f2)
    access_abc_f = pickle.load(f3)
    access_d_b = pickle.load(f4)
    access_a_f = pickle.load(f5)
    access_bcd_b = pickle.load(f6)
    value_ab_f = pickle.load(f7)
    value_cd_b = pickle.load(f8)
    value_abc_f = pickle.load(f11)
    value_d_b = pickle.load(f12)
    value_a_f = pickle.load(f9)
    value_bcd_b = pickle.load(f10)
    v_1 = pickle.load(f13)
    v_2 = pickle.load(f14)
    v_3 = pickle.load(f15)

    m_t_f = {}
    mmm = 0
    error = 0
    for key, val in ngram_4.items():
        try:
            improve = []
            times = []
            key_0 = key[0:1]
            key_123 = key[1:4]
            improve1 = np.power(ngram_4[key] / (v_1[key_0] + v_3[key_123]), 2) / (
                        (v_1[key_0] / total_word) * (v_3[key_123] / total_word))
            r1 = ngram_4[key] / value_a_f[key_0]
            r2 = ngram_4[key] / value_bcd_b[key_123]
            if r1 >= r2:
                times1 = r1 / (1 / access_a_f[key_0])
            else:
                times1 = r2 / (1 / access_bcd_b[key_123])
            improve.append(improve1)
            times.append(times1)
            key_01 = key[0:2]
            key_23 = key[2:4]
            improve2 = np.power(ngram_4[key] / (v_2[key_01] + v_2[key_23]), 2) / (
                    (v_2[key_01] / total_word) * (v_2[key_23] / total_word))
            r3 = ngram_4[key] / value_ab_f[key_01]
            r4 = ngram_4[key] / value_cd_b[key_23]
            if r3 >= r4:
                times2 = r3 / (1 / access_ab_f[key_01])
            else:
                times2 = r4 / (1 / access_cd_b[key_23])
            improve.append(improve2)
            times.append(times2)
            key_012 = key[0:3]
            key_3 = key[3:4]
            improve3 = np.power(ngram_4[key] / (v_3[key_012] + v_1[key_3]), 2) / (
                    (v_3[key_012] / total_word) * (v_1[key_3] / total_word))
            r5 = ngram_4[key] / value_abc_f[key_012]
            r6 = ngram_4[key] / value_d_b[key_3]
            if r5 >= r6:
                times3 = r5 / (1 / access_abc_f[key_012])
            else:
                times3 = r6 / (1 / access_d_b[key_3])
            improve.append(improve3)
            times.append(times3)
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
    print("\nkeyerror:", error)
    dump_path = l_path+"edge.pkl"
    f = open(dump_path, "wb")
    pickle.dump(m_t_f, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='pati computation')
    parser.add_argument('--corpus-path', type=str, default="/home/zyf/桌面/PFNE/data/corpus_wash.txt")
    parser.add_argument('--ngram-txt', type=str, default="/home/zyf/桌面/PFNE/ngram4.txt")
    parser.add_argument('--ngram-pkl', type=str, default="/home/zyf/桌面/PFNE/ngram4.pkl")
    parser.add_argument('--access-sum-path', type=str, default="/home/zyf/桌面/PFNE/ngram4/")
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













