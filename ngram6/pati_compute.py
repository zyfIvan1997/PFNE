
import pickle
import numpy as np
import argparse
import pickle


def access_sum(t_path, s_path):
    access_a_f = {}
    access_bcdef_b = {}
    access_ab_f = {}
    access_cdef_b = {}
    access_abc_f = {}
    access_def_b = {}
    access_abcd_f = {}
    access_ef_b = {}
    access_abcde_f = {}
    access_f_b = {}

    sum_a = {}
    sum_bcdef = {}
    sum_ab = {}
    sum_cdef = {}
    sum_abc = {}
    sum_def = {}
    sum_abcd = {}
    sum_ef = {}
    sum_abcde = {}
    sum_f = {}

    '''不考虑方向的 a/bcdef, ab/cdef, abc/def, abcd/ef, abcde/f 的 value信息'''
    v_1 = {}
    v_2 = {}
    v_3 = {}
    v_4 = {}
    v_5 = {}

    '''存储地址'''
    f1 = open(s_path+"access_a.pkl", "wb")
    f2 = open(s_path+"access_bcdef.pkl", "wb")
    f3 = open(s_path+"access_ab.pkl", "wb")
    f4 = open(s_path+"access_cdef.pkl", "wb")
    f5 = open(s_path+"access_abc.pkl", "wb")
    f6 = open(s_path+"access_def.pkl", "wb")
    f7 = open(s_path+"access_abcd.pkl", "wb")
    f8 = open(s_path+"access_ef.pkl", "wb")
    fa1 = open(s_path+"access_abcde.pkl", "wb")
    fa2 = open(s_path+"access_f.pkl", "wb")

    f9 = open(s_path+"sum_a.pkl", "wb")
    f10 = open(s_path+"sum_bcdef.pkl", "wb")
    f11 = open(s_path+"sum_ab.pkl", "wb")
    f12 = open(s_path+"sum_cdef.pkl", "wb")
    f13 = open(s_path+"sum_abc.pkl", "wb")
    f14 = open(s_path+"sum_def.pkl", "wb")
    f15 = open(s_path+"sum_abcd.pkl", "wb")
    f16 = open(s_path+"sum_ef.pkl", "wb")
    fs1 = open(s_path+"sum_abcde.pkl", "wb")
    fs2 = open(s_path+"sum_f.pkl", "wb")

    f17 = open(s_path+"v_1.pkl", "wb")
    f18 = open(s_path+"v_2.pkl", "wb")
    f19 = open(s_path+"v_3.pkl", "wb")
    f20 = open(s_path+"v_4.pkl", "wb")
    fv1 = open(s_path+"v_5.pkl", "wb")

    ff = open(t_path, "r")
    for line in ff:
        key = line.split(',')[0]
        val = int(line.split(',')[1])
        k_1 = key[0:1]
        k_23456 = key[1:6]
        k_12 = key[0:2]
        k_3456 = key[2:6]
        k_123 = key[0:3]
        k_456 = key[3:6]
        k_1234 = key[0:4]
        k_56 = key[4:6]
        k_12345 = key[0:5]
        k_6 = key[5:6]
        if k_1 not in access_a_f:
            access_a_f[k_1] = 1
            sum_a[k_1] = val
        else:
            access_a_f[k_1] += 1
            sum_a[k_1] += val
        if k_23456 not in access_bcdef_b:
            access_bcdef_b[k_23456] = 1
            sum_bcdef[k_23456] = val
        else:
            access_bcdef_b[k_23456] += 1
            sum_bcdef[k_23456] += val
        if k_12 not in access_ab_f:
            access_ab_f[k_12] = 1
            sum_ab[k_12] = val
        else:
            access_ab_f[k_12] += 1
            sum_ab[k_12] += val
        if k_3456 not in access_cdef_b:
            access_cdef_b[k_3456] = 1
            sum_cdef[k_3456] = val
        else:
            access_cdef_b[k_3456] += 1
            sum_cdef[k_3456] += val
        if k_123 not in access_abc_f:
            access_abc_f[k_123] = 1
            sum_abc[k_123] = val
        else:
            access_abc_f[k_123] += 1
            sum_abc[k_123] += val
        if k_456 not in access_def_b:
            access_def_b[k_456] = 1
            sum_def[k_456] = val
        else:
            access_def_b[k_456] += 1
            sum_def[k_456] += val
        if k_1234 not in access_abcd_f:
            access_abcd_f[k_1234] = 1
            sum_abcd[k_1234] = val
        else:
            access_abcd_f[k_1234] += 1
            sum_abcd[k_1234] += val
        if k_56 not in access_ef_b:
            access_ef_b[k_56] = 1
            sum_ef[k_56] = val
        else:
            access_ef_b[k_56] += 1
            sum_ef[k_56] += val
        if k_12345 not in access_abcde_f:
            access_abcde_f[k_12345] = 1
            sum_abcde[k_12345] = val
        else:
            access_abcde_f[k_12345] += 1
            sum_abcde[k_12345] += val
        if k_6 not in access_f_b:
            access_f_b[k_6] = 1
            sum_f[k_6] = val
        else:
            access_f_b[k_6] += 1
            sum_f[k_6] += val
        if k_1 not in v_1:
            v_1[k_1] = val
        else:
            v_1[k_1] += val
        if k_23456 not in v_5:
            v_5[k_23456] = val
        else:
            v_5[k_23456] += val
        if k_12 not in v_2:
            v_2[k_12] = val
        else:
            v_2[k_12] += val
        if k_3456 not in v_4:
            v_4[k_3456] = val
        else:
            v_4[k_3456] += val
        if k_123 not in v_3:
            v_3[k_123] = val
        else:
            v_3[k_123] += val
        if k_456 not in v_3:
            v_3[k_456] = val
        else:
            v_3[k_456] += val
        if k_1234 not in v_4:
            v_4[k_1234] = val
        else:
            v_4[k_1234] += val
        if k_56 not in v_2:
            v_2[k_56] = val
        else:
            v_2[k_56] += val
        if k_12345 not in v_5:
            v_5[k_12345] = val
        else:
            v_5[k_12345] += val
        if k_6 not in v_1:
            v_1[k_6] = val
        else:
            v_1[k_6] += val

    pickle.dump(access_a_f, f1)
    pickle.dump(access_bcdef_b, f2)
    pickle.dump(access_ab_f, f3)
    pickle.dump(access_cdef_b, f4)
    pickle.dump(access_abc_f, f5)
    pickle.dump(access_def_b, f6)
    pickle.dump(access_abcd_f, f7)
    pickle.dump(access_ef_b, f8)
    pickle.dump(access_abcde_f, fa1)
    pickle.dump(access_f_b, fa2)
    pickle.dump(sum_a, f9)
    pickle.dump(sum_bcdef, f10)
    pickle.dump(sum_ab, f11)
    pickle.dump(sum_cdef, f12)
    pickle.dump(sum_abc, f13)
    pickle.dump(sum_def, f14)
    pickle.dump(sum_abcd, f15)
    pickle.dump(sum_ef, f16)
    pickle.dump(sum_abcde, fs1)
    pickle.dump(sum_f, fs2)
    pickle.dump(v_1, f17)
    pickle.dump(v_2, f18)
    pickle.dump(v_3, f19)
    pickle.dump(v_4, f20)
    pickle.dump(v_5, fv1)
    ff.close()
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    fa1.close()
    fa2.close()
    f9.close()
    f10.close()
    f11.close()
    f12.close()
    f13.close()
    f14.close()
    f15.close()
    f16.close()
    fs1.close()
    fs2.close()
    f17.close()
    f18.close()
    f19.close()
    f20.close()
    fv1.close()


def mp_at_f(p_path, c_path, l_path):
    f = open(p_path, "rb")
    ngram_4 = pickle.load(f)
    s_n = len(ngram_4)
    f = open(c_path, "r")
    total_word = len(f.read())
    print(total_word)

    f1 = open(l_path+"access_a.pkl", "rb")
    f2 = open(l_path+"access_bcdef.pkl", "rb")
    f3 = open(l_path+"access_ab.pkl", "rb")
    f4 = open(l_path+"access_cdef.pkl", "rb")
    f5 = open(l_path+"access_abc.pkl", "rb")
    f6 = open(l_path+"access_def.pkl", "rb")
    fa1 = open(l_path+"access_abcd.pkl", "rb")
    fa2 = open(l_path+"access_ef.pkl", "rb")
    fa3 = open(l_path+"access_abcde.pkl", "rb")
    fa4 = open(l_path+"access_f.pkl", "rb")

    f7 = open(l_path+"sum_a.pkl", "rb")
    f8 = open(l_path+"sum_bcdef.pkl", "rb")
    f9 = open(l_path+"sum_ab.pkl", "rb")
    f10 = open(l_path+"sum_cdef.pkl", "rb")
    f11 = open(l_path+"sum_abc.pkl", "rb")
    f12 = open(l_path+"sum_def.pkl", "rb")
    fs1 = open(l_path+"sum_abcd.pkl", "rb")
    fs2 = open(l_path+"sum_ef.pkl", "rb")
    fs3 = open(l_path+"sum_abcde.pkl", "rb")
    fs4 = open(l_path+"sum_f.pkl", "rb")

    f13 = open(l_path+"v_1.pkl", "rb")
    f14 = open(l_path+"v_2.pkl", "rb")
    f15 = open(l_path+"v_3.pkl", "rb")
    fv1 = open(l_path+"v_4.pkl", "rb")
    fv2 = open(l_path+"v_5.pkl", "rb")

    access_a_f = pickle.load(f1)
    access_bcdef_b = pickle.load(f2)
    access_ab_f = pickle.load(f3)
    access_cdef_b = pickle.load(f4)
    access_abc_f = pickle.load(f5)
    access_def_b = pickle.load(f6)
    access_abcd_f = pickle.load(fa1)
    access_ef_b = pickle.load(fa2)
    access_abcde_f = pickle.load(fa3)
    access_f_b = pickle.load(fa4)
    value_a_f = pickle.load(f7)
    value_bcdef_b = pickle.load(f8)
    value_ab_f = pickle.load(f9)
    value_cdef_b = pickle.load(f10)
    value_abc_f = pickle.load(f11)
    value_def_b = pickle.load(f12)
    value_abcd_f = pickle.load(fs1)
    value_ef_b = pickle.load(fs2)
    value_abcde_f = pickle.load(fs3)
    value_f_b = pickle.load(fs4)
    v_1 = pickle.load(f13)
    v_2 = pickle.load(f14)
    v_3 = pickle.load(f15)
    v_4 = pickle.load(fv1)
    v_5 = pickle.load(fv2)
    m_t_f = {}
    mmm = 0
    error = 0
    for key, val in ngram_4.items():
        try:
            improve = []
            times = []
            key_0 = key[0:1]
            key_12345 = key[1:6]
            improve1 = np.power(ngram_4[key] / (v_1[key_0] + v_5[key_12345]), 2) / (
                        (v_1[key_0] / total_word) * (v_5[key_12345] / total_word))
            r1 = ngram_4[key] / value_a_f[key_0]
            r2 = ngram_4[key] / value_bcdef_b[key_12345]
            if r1 >= r2:
                times1 = r1 / (1 / access_a_f[key_0])
            else:
                times1 = r2 / (1 / access_bcdef_b[key_12345])
            improve.append(improve1)
            times.append(times1)

            key_01 = key[0:2]
            key_2345 = key[2:6]
            improve2 = np.power(ngram_4[key] / (v_2[key_01] + v_4[key_2345]), 2) / (
                        (v_2[key_01] / total_word) * (v_4[key_2345] / total_word))
            r3 = ngram_4[key] / value_ab_f[key_01]
            r4 = ngram_4[key] / value_cdef_b[key_2345]
            if r3 >= r4:
                times2 = r3 / (1 / access_ab_f[key_01])
            else:
                times2 = r4 / (1 / access_cdef_b[key_2345])
            improve.append(improve2)
            times.append(times2)

            key_012 = key[0:3]
            key_345 = key[3:6]
            improve3 = np.power(ngram_4[key] / (v_3[key_012] + v_3[key_345]), 2) / (
                        (v_3[key_012] / total_word) * (v_3[key_345] / total_word))
            r5 = ngram_4[key] / value_abc_f[key_012]
            r6 = ngram_4[key] / value_def_b[key_345]
            if r5 >= r6:
                times3 = r5 / (1 / access_abc_f[key_012])
            else:
                times3 = r6 / (1 / access_def_b[key_345])
            improve.append(improve3)
            times.append(times3)

            key_0123 = key[0:4]
            key_45 = key[4:6]
            improve4 = np.power(ngram_4[key] / (v_4[key_0123] + v_2[key_45]), 2) / (
                        (v_4[key_0123] / total_word) * (v_2[key_45] / total_word))
            r7 = ngram_4[key] / value_abcd_f[key_0123]
            r8 = ngram_4[key] / value_ef_b[key_45]
            if r7 >= r8:
                times4 = r7 / (1 / access_abcd_f[key_0123])
            else:
                times4 = r8 / (1 / access_ef_b[key_45])
            improve.append(improve4)
            times.append(times4)

            key_01234 = key[0:5]
            key_5 = key[5:6]
            improve5 = np.power(ngram_4[key] / (v_5[key_01234] + v_1[key_5]), 2) / (
                        (v_5[key_01234] / total_word) * (v_1[key_5] / total_word))
            r9 = ngram_4[key] / value_abcde_f[key_01234]
            r10 = ngram_4[key] / value_f_b[key_5]
            if r9 >= r10:
                times5 = r9 / (1 / access_abcde_f[key_01234])
            else:
                times5 = r10 / (1 / access_f_b[key_5])
            improve.append(improve5)
            times.append(times5)

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
    parser.add_argument('--ngram-txt', type=str, default="/home/zyf/桌面/PFNE/ngram6.txt")
    parser.add_argument('--ngram-pkl', type=str, default="/home/zyf/桌面/PFNE/ngram6.pkl")
    parser.add_argument('--access-sum-path', type=str, default="/home/zyf/桌面/PFNE/ngram6/")
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













