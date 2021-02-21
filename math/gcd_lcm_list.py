from functools import reduce
from math import gcd

# 複数(リスト)から最大公約数
def gcd_list(num_list: list) -> int:
    return reduce(gcd, num_list)

# 複数(リスト)から最小公倍数(計算量:Nlog(maxXi))
def lcm_base(x: int, y: int) -> int:
    return (x * y) // gcd(x, y)
def lcm_list(num_list: list):
    return reduce(lcm_base, num_list, 1)