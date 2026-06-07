class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        maxCount = 0
        l = 0
        for r in range(len(s)):
            if (s[r] in charset):
                while (s[r] in charset):
                    charset.remove(s[l])
                    l += 1
            charset.add(s[r])
            maxCount = max(maxCount, len(charset))
        return maxCount
                    