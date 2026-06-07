class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Solution: Use a dictionary to keep track of max frequency
        # Once window length - max F > k => slide window 
        count = {}
        longest = 0
        l = 0
        for r in range(len(s)):
            # Populate the dictionary of char frequency:
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(count.values())
            if (r - l + 1 - maxF > k):
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest