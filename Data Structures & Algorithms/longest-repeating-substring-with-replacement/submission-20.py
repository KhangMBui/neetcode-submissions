class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Solution: Use a dictionary count to keep track of maximum frequency
        # Once window length - max F > k => Slide window
        count = {}
        longest = 0
        l = 0
        for r in range(len(s)):
            # Populate the dict:
            count[s[r]] = 1 + count.get(s[r], 0)
            if (r - l + 1 - max(count.values()) > k):
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest