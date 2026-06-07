class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        l, r = 0, 0
        res = 0
        while r < len(s):
            if s[r] in s[l:r]:
                l += 1
                r = l
            else:
                res = max(res, r - l + 1)
                r += 1
        return res
        