from bisect import bisect_right

# LIS(最長増加部分列)
# num_list: 対象リスト
# resurn: LISになっていないことに注意！あくまでLISの文字列数！
# https://wakabame.hatenablog.com/entry/2017/08/27/210846
def LIS(num_list: list) -> int:
    result_list = []
    for num in num_list:
        insert_index = bisect_right(result_list, num)
        if len(result_list) == insert_index:
            result_list.append(num)
        else:
            result_list[insert_index] = num

    return len(result_list)