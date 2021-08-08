class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        while x != 0:
            res = res * 10 + x % 10
            x //= 10
        return res * sign if (-2**31) <= res <= 2**31 - 1 else 0