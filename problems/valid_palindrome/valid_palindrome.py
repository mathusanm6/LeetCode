def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    s = s.lower()

    while left < right:
        s_l, s_r = s[left], s[right]

        if not s_l.isalnum():
            left += 1
            continue

        if not s_r.isalnum():
            right -= 1
            continue

        if s_l != s_r:
            return False

        left += 1
        right -= 1
    return True
