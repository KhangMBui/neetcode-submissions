# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n < 1:
            raise Exception("invalid input")
        
        l, r = 1, n

        while l <= r:
            m = (l + r) // 2

            if guess(m) == 0:
                return m
            
            elif guess(m) == -1: # higher
                r = m - 1
            else: # guess(m) == 1 # lower
                l = m + 1
        return -1