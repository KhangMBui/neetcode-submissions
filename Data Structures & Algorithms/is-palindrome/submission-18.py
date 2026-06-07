class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalnum(c):
            return '0' <= c <= '9' or 'a' <= c.lower() <= 'z'
        # Two pointers:
        l, r = 0, len(s) - 1
        while (l < r):
            while l < r and not isalnum(s[l]):
                l += 1
            while l < r and not isalnum(s[r]):
                r -= 1
            if (s[l].lower() != s[r].lower()):
                return False
            l += 1
            r -= 1
        return True