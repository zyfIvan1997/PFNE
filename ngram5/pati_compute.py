
import pickle
import numpy as np
import argparse
import pickle


def access_sum(t_path, s_path):
    access_a_f = {}
    access_bcde_b = {}
    access_ab_f = {}
    access_cde_b = {}
    access_abc_f = {}
    access_de_b = {}
    access_abcd_f = {}
    access_e_b = {}
    sum_a = {}
    sum_bcde = {}
    sum_ab = {}
    sum_cde = {}
    sum_abc = {}
    sum_de = {}
    sum_abcd = {}
    sum_e = {}
    v_1 = {}
    v_2 = {}
    v_3 = {}
    v_4 = {}
    f1 = open(s_path+"access_a.pkl", "wb")
    f2 = open(s_path+"access_bcde.pkl", "wb")
    f3 = open(s_path+"access_ab.pkl", "wb")
    f4 = open(s_path+"access_cde.pkl", "wb")
    f5 = open(s_path+"access_abc.pkl", "wb")
    f6 = open(s_path+"access_de.pkl", "wb")
    f7 = open(s_path+"access_abcd.pkl", "wb")
    f8 = open(s_path+"access_e.pkl", "wb")
    f9 = open(s_path+"sum_a.pkl", "wb")
    f10 = open(s_path+"sum_bcde.pkl", "wb")
    f11 = open(s_path+"sum_ab.pkl", "wb")
    f12 = open(s_path+"sum_cde.pkl", "wb")
    f13 = open(s_path+"sum_abc.pkl", "wb")
    f14 = open(s_path+"sum_de.pkl", "wb")
    f15 = open(s_path+"sum_abcd.pkl", "wb")
    f16 = open(s_path+"sum_e.pkl", "wb")

    f17 = open(s_path+"v_1.pkl", "wb")
    f18 = open(s_path+"v_2.pkl", "wb")
    f19 = open(s_path+"v_3.pkl", "wb")
    f20 = open(s_path+"v_4.pkl", "wb")

    ff = open(t_path, "r")
    for line in ff:
        key = line.split(',')[0]
        val = int(line.split(',')[1])
        k_1 = key[0:1]
        k_2345 = key[1:5]
        k_12 = key[0:2]
        k_345 = key[2:5]
        k_123 = key[0:3]
        k_45 = key[3:5]
        k_1234 = key[0:4]
        k_5 = key[4:5]
        if k_1 not in access_a_f:
            access_a_f[k_1] = 1
            sum_a[k_1] = val
        else:
            access_a_f[k_1] += 1
            sum_a[k_1] += val
        if k_2345 not in access_bcde_b:
            access_bcde_b[k_2345] = 1
            sum_bcde[k_2345] = val
        else:
            access_bcde_b[k_2345] += 1
            sum_bcde[k_2345] += val
        if k_12 not in access_ab_f:
            access_ab_f[k_12] = 1
            sum_ab[k_12] = val
        else:
            access_ab_f[k_12] += 1
            sum_ab[k_12] += val
        if k_345 not in access_cde_b:
            access_cde_b[k_345] = 1
            sum_cde[k_345] = val
        else:
            access_cde_b[k_345] += 1
            sum_cde[k_345] += val
        if k_123 not in access_abc_f:
            access_abc_f[k_123] = 1
            sum_abc[k_123] = val
        else:
            access_abc_f[k_123] += 1
            sum_abc[k_123] += val
        if k_45 not in access_de_b:
            access_de_b[k_45] = 1
            sum_de[k_45] = val
        else:
            access_de_b[k_45] += 1
            sum_de[k_45] += val
        if k_1234 not in access_abcd_f:
            access_abcd_f[k_1234] = 1
            sum_abcd[k_1234] = val
        else:
            access_abcd_f[k_1234] += 1
            sum_abcd[k_1234] += val
        if k_5 not in access_e_b:
            access_e_b[k_5] = 1
            sum_e[k_5] = val
        else:
            access_e_b[k_5] += 1
            sum_e[k_5] += val
        if k_1 not in v_1:
            v_1[k_1] = val
        else:
            v_1[k_1] += val
        if k_2345 not in v_4:
            v_4[k_2345] = val
        else:
            v_4[k_2345] += val
        if k_12 not in v_2:
            v_2[k_12] = val
        else:
            v_2[k_12] += val
        if k_345 not in v_3:
            v_3[k_345] = val
        else:
            v_3[k_345] += val
        if k_123 not in v_3:
            v_3[k_123] = val
        else:
            v_3[k_123] += val
        if k_45 not in v_2:
            v_2[k_45] = val
        else:
            v_2[k_45] += val
        if k_1234 not in v_4:
            v_4[k_1234] = val
        else:
            v_4[k_1234] += val
        if k_5 not in v_1:
            v_1[k_5] = val
        else:
            v_1[k_5] += val
    pickle.dump(access_a_f, f1)
    pickle.dump(access_bcde_b, f2)
    pickle.dump(access_ab_f, f3)
    pickle.dump(access_cde_b, f4)
    pickle.dump(access_abc_f, f5)
    pickle.dump(access_de_b, f6)
    pickle.dump(access_abcd_f, f7)
    pickle.dump(access_e_b, f8)
    pickle.dump(sum_a, f9)
    pickle.dump(sum_bcde, f10)
    pickle.dump(sum_ab, f11)
    pickle.dump(sum_cde, f12)
    pickle.dump(sum_abc, f13)
    pickle.dump(sum_de, f14)
    pickle.dump(sum_abcd, f15)
    pickle.dump(sum_e, f16)
    pickle.dump(v_1, f17)
    pickle.dump(v_2, f18)
    pickle.dump(v_3, f19)
    pickle.dump(v_4, f20)
    ff.close()
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    f9.close()
    f10.close()
    f11.close()
    f12.close()
    f13.close()
    f14.close()
    f15.close()
    f16.close()
    f17.close()
    f18.close()
    f19.close()
    f20.close()


def mp_at_f(p_path, c_path, l_path):
    f = open(p_path, "rb")
    ngram_4 = pickle.load(f)
    s_n = len(ngram_4)
    f = open(c_path, "r")
    total_word = len(f.read())
    print(total_word)

    f1 = open(l_path+"access_a.pkl", "rb")
    f2 = open(l_path+"access_bcde.pkl", "rb")
    f3 = open(l_path+"access_ab.pkl", "rb")
    f4 = open(l_path+"access_cde.pkl", "rb")
    f5 = open(l_path+"access_abc.pkl", "rb")
    f6 = open(l_path+"access_de.pkl", "rb")
    fa1 = open(l_path+"access_abcd.pkl", "rb")
    fa2 = open(l_path+"access_e.pkl", "rb")
    f7 = open(l_path+"sum_a.pkl", "rb")
    f8 = open(l_path+"sum_bcde.pkl", "rb")
    f9 = open(l_path+"sum_ab.pkl", "rb")
    f10 = open(l_path+"sum_cde.pkl", "rb")
    f11 = open(l_path+"sum_abc.pkl", "rb")
    f12 = open(l_path+"sum_de.pkl", "rb")
    fs1 = open(l_path+"sum_abcd.pkl", "rb")
    fs2 = open(l_path+"sum_e.pkl", "rb")
    f13 = open(l_path+"v_1.pkl", "rb")
    f14 = open(l_path+"v_2.pkl", "rb")
    f15 = open(l_path+"v_3.pkl", "rb")
    fv1 = open(l_path+"v_4.pkl", "rb")

    access_a_f = pickle.load(f1)
    access_bcde_b = pickle.load(f2)
    access_ab_f = pickle.load(f3)
    access_cde_b = pickle.load(f4)
    access_abc_f = pickle.load(f5)
    access_de_b = pickle.load(f6)
    access_abcd_f = pickle.load(fa1)
    access_e_b = pickle.load(fa2)
    print("#########access load complete###############")
    value_a_f = pickle.load(f7)
    value_bcde_b = pickle.load(f8)
    value_ab_f = pickle.load(f9)
    value_cde_b = pickle.load(f10)
    value_abc_f = pickle.load(f11)
    value_de_b = pickle.load(f12)
    value_abcd_f = pickle.load(fs1)
    value_e_b = pickle.load(fs2)
    print("#########sum load complete##################")
    v_1 = pickle.load(f13)
    v_2 = pickle.load(f14)
    v_3 = pickle.load(f15)
    v_4 = pickle.load(fv1)

    m_t_f = {}
    mmm = 0
    error = 0
    for key, val in ngram_4.items():
        try:
            improve = []
            times = []

            key_0 = key[0:1]
            key_1234 = key[1:5]
            improve1 = np.power(ngram_4[key] / (v_1[key_0] + v_4[key_1234]), 2) / (
                        (v_1[key_0] / total_word) * (v_4[key_1234] / total_word))
            r1 = ngram_4[key] / value_a_f[key_0]
            r2 = ngram_4[key] / value_bcde_b[key_1234]
            if r1 >= r2:
                times1 = r1 / (1 / access_a_f[key_0])
            else:
                times1 = r2 / (1 / access_bcde_b[key_1234])
            improve.append(improve1)
            times.append(times1)

            key_01 = key[0:2]
            key_234 = key[2:5]
            improve2 = np.power(ngram_4[key] / (v_2[key_01] + v_3[key_234]), 2) / (
                        (v_2[key_01] / total_word) * (v_3[key_234] / total_word))
            r3 = ngram_4[key] / value_ab_f[key_01]
            r4 = ngram_4[key] / value_cde_b[key_234]
            if r3 >= r4:
                times2 = r3 / (1 / access_ab_f[key_01])
            else:
                times2 = r4 / (1 / access_cde_b[key_234])
            improve.append(improve2)
            times.append(times2)

            key_012 = key[0:3]
            key_34 = key[3:5]
            improve3 = np.power(ngram_4[key] / (v_3[key_012] + v_2[key_34]), 2) / (
                        (v_3[key_012] / total_word) * (v_2[key_34] / total_word))
            r5 = ngram_4[key] / value_abc_f[key_012]
            r6 = ngram_4[key] / value_de_b[key_34]
            if r5 >= r6:
                times3 = r5 / (1 / access_abc_f[key_012])
            else:
                times3 = r6 / (1 / access_de_b[key_34])
            improve.append(improve3)
            times.append(times3)

            key_0123 = key[0:4]
            key_4 = key[4:5]
            improve4 = np.power(ngram_4[key] / (v_4[key_0123] + v_1[key_4]), 2) / (
                        (v_4[key_0123] / total_word) * (v_1[key_4] / total_word))
            r7 = ngram_4[key] / value_abcd_f[key_0123]
            r8 = ngram_4[key] / value_e_b[key_4]
            if r7 >= r8:
                times4 = r7 / (1 / access_abcd_f[key_0123])
            else:
                times4 = r8 / (1 / access_e_b[key_4])
            improve.append(improve4)
            times.append(times4)

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
    parser.add_argument('--ngram-txt', type=str, default="/home/zyf/桌面/PFNE/ngram5.txt")
    parser.add_argument('--ngram-pkl', type=str, default="/home/zyf/桌面/PFNE/ngram5.pkl")
    parser.add_argument('--access-sum-path', type=str, default="/home/zyf/桌面/PFNE/ngram5/")
    parser.add_argument('--min-count', type=int, default=1)
    parser.add_argument('--ngram-word', type=str, default="/home/zyf/桌面/PFNE/embedding/ngram_word.txt")
    parser.add_argument('--ngram-count', type=str, default="/home/zyf/桌面/PFNE/embedding/ngram_count.txt")
    parser.add_argument('--voca-size', type=int, default=50000)
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













