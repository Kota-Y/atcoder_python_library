from math import floor, sqrt

# 素数判定(何回も判定する時用)
# 最初に素数リストをつくっておいて高速化する
def check_multi_prime(n: int, prime_list: list) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
  
    m = floor(sqrt(n))
    for p in prime_list:
        if n % p == 0:
            return False
        if p > m:
            # 素数がnの平方根を超えたら終了
            break
    return True

# 高速に素数リスト作成
# 0からNまでの素数リストを作成する(計算量はオーダーN、ただし10**8は通らない、10**7までは通る)
# 参照 https://ikatakos.com/pot/programming_algorithm/number_theory/prime_judge
def create_prime_list(n: int) -> list:
    primes = [0, 1] * (n // 2 + 1)
    if n % 2 == 0:
        primes.pop()
    primes[1] = 0
    primes[2] = 1
    for p in range(3, n + 1, 2):
        if primes[p]:
            for q in range(p * p, n + 1, 2 * p):
                primes[q] = 0

    prime_list = []
    for i, p in enumerate(primes):
        if p == 1:
            prime_list.append(i)
    
    return prime_list