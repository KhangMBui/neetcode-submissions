class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Solution: keep track of the most frequent character using a dict
        # Once windowLength - mostFreq > k: slide the window
        
        # Initialize the dict to keep track of most freq char:
        count = {}
        # Initialize the result variable:
        longest = 0
        # Initialize the left position of the sliding window:
        l = 0
        
        # Iterate the string with the right pointer:
        for r in range(len(s)):
            # Add to dict:
            count[s[r]] = 1 + count.get(s[r], 0)
            # Check condition to move sliding window
            while (r - l + 1) - (max(count.values())) > k:
                count[s[l]] -= 1
                l += 1
            # Calculate the longest:
            longest = max(longest, r - l + 1)
        # Return the result
        return longest