MOD = 10 ** 9 + 7

# 組み合わせ計算(nCr、MODが素数のときに高速に計算できる)
# factorial、inverseを事前に作成しておくことで可能！
# https://atcoder.jp/contests/abc151/tasks/abc151_e
# https://ikatakos.com/pot/programming_algorithm/number_theory/mod_combination
def combination_mod(n: int, r: int, factorial: list, inverse: list) -> int:
    if n < r or r < 0:
        return 0
    elif r == 0:
        return 1
    return factorial[n] * inverse[r] * inverse[n - r] % MOD

# 階乗と逆元テーブルを事前計算
factorial = [1]
inverse = [1]
for i in range(1, n+2):
    factorial.append(factorial[-1] * i % MOD)
    inverse.append(pow(factorial[-1], MOD - 2, MOD))