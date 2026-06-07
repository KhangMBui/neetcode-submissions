class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Solution: Create a set of character to keep track
        charSet = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while (s[r] in charSet):
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            longest = max(longest, r - l + 1)
        return longest

            