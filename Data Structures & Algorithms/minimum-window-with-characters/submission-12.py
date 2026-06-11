class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count_t = Counter(t)
        count_s = {}

        have = 0
        need = len(count_t)

        res = [-1, -1]
        res_len = float("inf")

        l = 0

        for r in range(len(s)):
            count_s[s[r]] = count_s.get(s[r], 0) + 1
            # If current character is what we need:
            if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
                # Increment have:
                have += 1
            
            # Once our have = need (we have the substring needed), attempt minimizing the window
            while have == need:
                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        
        left, right = res
        if res_len == float("inf"):
            return ""

        return s[left:right+1]
                
        