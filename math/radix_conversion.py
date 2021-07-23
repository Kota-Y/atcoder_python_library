# n進数から10進数に変換
# baseは2から36までの整数を指定
def Base_n_to_10(value: int, base: int) -> int:
    return int(str(value), base)

# 10進数からn進数に変換
def Base_10_to_n(value: int, base: int) -> int:
    nine_number = ""
    while value > 0:
        nine_number += str(value % base)
        value //= base
    return int(nine_number[::-1])