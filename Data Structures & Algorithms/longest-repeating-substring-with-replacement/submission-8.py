class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Solution: keep track of the most frequent character
        # once windowLength - mostFreq > k : move left up
        l = 0
        longest = 0
        count = {}
        for r in range(len(s)):
            # Update the count dictionary:
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1 - max(count.values()) > k):
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest