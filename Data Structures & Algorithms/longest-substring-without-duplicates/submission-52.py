class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use a sliding window that, whenever we found a character
        # that's already in our progressive string, then we shrink the left side
        if not s:
            return 0

        longest = 0
        l = 0
        uniques = set()

        for r in range(len(s)):
            while s[r] in uniques:
                uniques.remove(s[l])
                l += 1
            
            longest = max(longest, r - l + 1)
            uniques.add(s[r])
        return longest