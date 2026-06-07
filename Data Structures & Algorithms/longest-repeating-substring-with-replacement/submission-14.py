class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Solution: Keeps track of most frequent character (maxF)
        # using a dictionary. Once windowLength - maxF > k => slide window

        # Initialize the dictionary
        count = {}
        longest = 0
        l = 0
        for r in range(len(s)):
            # Loading data into the dictionary
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest