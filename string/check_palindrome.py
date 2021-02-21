# 回文判定
def check_palindrome(s: str) -> bool:
    if s == s[::-1]:
        return True
    else:
        return False