class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # For a given substring, always optimal 
        # to replace characters the most frequent character in that substring
        # because it will minimizes the number of replacements required
        # to make all characters in the string identical
        # Formula: current substring size - maxF > k => shrink l
        # if <= k: store result
        if not s:
            return 0
        
        # Intialize window left side
        l = 0
        # Intialize dictionary to count character
        count = {}
        # Initialize longest count variable
        longest = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            # window_size = r - l + 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest

