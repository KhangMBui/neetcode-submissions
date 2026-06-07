class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        # Initialize a dict countT to keep track of what we need
        # and a dict window for our sliding window
        countT, window = {}, {}
        # Load data into countT:
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        # Initialize the amount of what we have & what we need
        have, need = 0, len(countT)
        # Initialize the result window and result length:
        res, resLen = [-1, -1], float("infinity")
        # Left pointer
        l = 0
        # Iterate through s, collecting words and iterating 'have'
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            # Increment 'have' if the word match
            if (s[r] in countT and countT[s[r]] == window[s[r]]):
                have += 1
            # Once have = need, we move sliding window
            while (have == need):
                # Store result first
                res = [l, r]
                resLen = min(resLen, r - l + 1)
                window[s[l]] -= 1
                if (s[l] in countT and window[s[l]] < countT[s[l]]):
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
