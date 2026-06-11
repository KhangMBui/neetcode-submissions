class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # "OUZODYXAZV" & "XYZ"
        # On the left side, as long as the character is not in t, we can move it up
        # On the right side, we keep moving it forward
        # Anytime we have matching maps (enough characters in t), we store data

        # Overall plan:
        # intialize a result empty string to store data and return at the end
        # create a hashmap for t characters
        # assign 0 to left pointer
        # let right pointer iterate through the string, creating a loop
        # inside the loop:
        #   as long as left pointer char not in t, we move l forward
        #   we keep moving r forward and put all characters in a hashmap
        #   anytime s hashmap = t hashmap, we store data 
        if len(s) < len(t):
            return ""
        
        t_count = Counter(t)
        s_count = {}

        have = 0
        need = len(t_count)

        res = [-1, -1]
        res_len = float("inf")

        l = 0
        for r in range(len(s)):
            s_count[s[r]] = s_count.get(s[r], 0) + 1

            # If this char is required and we now have enough of it:
            if s[r] in t_count and s_count[s[r]] == t_count[s[r]]:
                have += 1
            
            # While current window is valid, try to shrink it
            while have == need:
                window_len = r - l + 1

                if window_len < res_len:
                    res = [l, r]
                    res_len = window_len
                
                # Remove left character from window:
                s_count[s[l]] -= 1

                # If removing it makes the window invalid
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                
                l += 1
        
        left, right = res
        if res_len == float("inf"):
            return ""
        return s[left:right + 1]

        