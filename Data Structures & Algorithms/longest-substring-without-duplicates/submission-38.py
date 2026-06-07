class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Solution: Use charset and sliding window
        # to keep track of seen characters
        # Traverse through the string and collect characters
        # into the set, once we meet a seen character, we move
        # the left edge of the sliding window up until it's
        # not seen anymore, while also keeping track of the longest
        # string
        seen = set()
        l = r = 0
        longest = 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, len(seen))
            r += 1
        return longest
                
