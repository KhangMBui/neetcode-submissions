
class Solution:
    def minWindow(self, s: str, t: str) -> str:
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
            char = s[r]
            s_count[char] = s_count.get(char, 0) + 1

            # If this char is required and we now have enough of it
            if char in t_count and s_count[char] == t_count[char]:
                have += 1

            # While current window is valid, try to shrink it
            while have == need:
                window_len = r - l + 1

                if window_len < res_len:
                    res = [l, r]
                    res_len = window_len

                # Remove left character from window
                left_char = s[l]
                s_count[left_char] -= 1

                # If removing it makes the window invalid
                if left_char in t_count and s_count[left_char] < t_count[left_char]:
                    have -= 1

                l += 1

        left, right = res

        if res_len == float("inf"):
            return ""

        return s[left:right + 1]