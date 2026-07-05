class Solution:
    def mySqrt(self, x: int) -> int:
        # return sqrt(x) rounded down to nearest integer

        if x <= 0:
            return 0

        l, r = 1, x
        res = 0

        while l <= r:
            m = (l + r) // 2

            square = m * m

            if square == x:
                return m
            elif square < x:
                l = m + 1
                res = m
            else: # square > x
                r = m - 1
        return res