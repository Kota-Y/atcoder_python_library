from math import floor, sqrt

def check_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    m = floor(sqrt(n)) + 1
    for p in range(3, m, 2):
        if n % p == 0:
            return False
    return True