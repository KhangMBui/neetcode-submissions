class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Solution: create a charset and left and right pointers
        #As we iterate through the string, while the next character
        #still exists in the string, we move the head of the string up
        # and calculate longest
        charSet = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            while (s[r] in charSet):
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            longest = max(longest, r - l + 1)
        return longest