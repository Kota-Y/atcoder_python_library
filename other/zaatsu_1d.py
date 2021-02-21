from copy import deepcopy

# 座圧圧縮(1次元)、オーダー(NlogN)
# https://atcoder.jp/contests/abc036/tasks/abc036_c
def zaatu1d(before_list: list) -> list:
    before_list_tmp = list(set(deepcopy(before_list)))
    before_list_tmp.sort()

    d = dict()
    for i in range(len(before_list_tmp)):
        d[before_list_tmp[i]] = i 

    after_list = []
    for before in before_list:
        after_list.append(d[before])

    return after_list