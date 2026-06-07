class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Solution: Use a dictionary to keep track of the most
        # frequently appeared character.
        # "XYYYX", k = 3 => "XXXXX"; maxF = 3
        # window_size - maxF = 5 - 3 = 2 <= k => good.
        # window_size - maxF <= k
        # Result will be the window_size
        # AABABBA
        # 
        if not s:
            return 0
        count = {} # Keeps track of character frequency
        longest = 0 # Longest window_size
        l = 0
        for r in range(len(s)):
            # Populate the dictionary:
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(count.values())
            while r - l + 1 - maxF > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
            
