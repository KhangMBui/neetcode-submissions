class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Check if t is empty
        if t == "":
            return ""
        # Create 2 dicts: 1 to keeps track of t, the other 
        # for the sliding window's characters
        countT, window = {}, {}
        # Initialize the t dictionary
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        # res to keep track of l and r, resLen to keep track of its length
        res, resLen = [-1, -1], float("infinity")
        # Initialize what we have and what we need
        have, need = 0, len(countT)
        # left pointer
        l = 0
        # Iterate the s string with the right pointer
        for r in range(len(s)):
            # Add it to the sliding window
            window[s[r]] = 1 + window.get(s[r], 0)
            # Check condition to add it to 'have':
            if (s[r] in countT and window[s[r]] == countT[s[r]]):
                have += 1
            # If have == need, we keeps track of the result and 
            # move the sliding window

            while (have == need):
                if (r - l + 1 < resLen):
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if (s[l] in countT and window[s[l]] < countT[s[l]]):
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
                
