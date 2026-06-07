class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Solution: use a dict Count to keep track of max frequency
        # Once window length - max frequency > k => Slide window
        count = {}
        l = 0
        result = 0
        for r in range(len(s)):
            # Populate the dictionary:
            count[s[r]] = 1 + count.get(s[r], 0)
            if (r - l + 1 - max(count.values()) > k):
                count[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result