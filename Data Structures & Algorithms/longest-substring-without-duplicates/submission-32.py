class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        charset = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            while (s[r] in charset):
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            longest = max(longest, len(charset))
        return longest
            