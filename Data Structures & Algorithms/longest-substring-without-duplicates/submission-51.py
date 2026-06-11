class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        uniques = set()
        longest = 0
        l = 0

        for r in range(len(s)):
            while s[r] in uniques:
                uniques.remove(s[l])
                l += 1
            uniques.add(s[r])
            longest = max(longest, r - l + 1)
        return longest

    
        