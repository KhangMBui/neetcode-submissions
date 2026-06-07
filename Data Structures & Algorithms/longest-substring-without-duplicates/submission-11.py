class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            # If same char already in the set
            # we move our sliding window rightward
            while (s[r] in charset):
                charset.remove(s[l])
                l += 1
            # add r to the charset and calculate longest
            charset.add(s[r])
            longest = max(longest, r - l + 1)
        return longest