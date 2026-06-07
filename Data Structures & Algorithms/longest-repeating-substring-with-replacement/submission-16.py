class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Solution: keep track of the maximum frequency of a character
        # once window length - maximum frequency > k => move window

        # Dict to keep track of frequency of characters
        count = {}
        # result var
        longest = 0
        # left pointer
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            # maximum frequency in the dictionary:
            maxF = max(count.values())
            # once window length - maximum frequency > k => move window
            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
               