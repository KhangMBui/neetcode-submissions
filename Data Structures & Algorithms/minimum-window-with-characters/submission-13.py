class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Overall plan: 
        # have a count_t to keep character frequency of t
        # have a count_s to keep character frequency of current substring in s

        # have a 'have' to count the current matching characters we have
        # and a 'need' to count the matching unique characters we need (from count_t)

        # an array 'res' with 2 indexes to keep position of 2 ends of sliding window
        #       the purpose is for us to return the substring with slicing at the end
        # and 'res_len' to keep track of res's length
        #       the purpose is compare string's length, as we want to minimize our result length

        # We'll initialize left pointer = 0, and use right pointer to iterate the string
        # Each time, we update count_s
        # If the character is in count_t (what we need), and count_s[that_char] == count_t[that_char]:
        #       That means we fulfilled one unique character. Increment 'have'
        # While have == need (we already have the full substring), store the data and attempt minimizing the window
        #       Store the data.
        #       Then attempt minimizing the window:
        #           firstly, decrement left pointer value from the hashmap count_s
        #           if that character is also in count_t, and count_s[that_char] < count_t[that_char]:
        #               decrement 'have'
        #       then increment left pointer

        # At the end, return s[left pointer : right pointer + 1]

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
            if s[r] in t_count and s_count[s[r]] == t_count[s[r]]:
                have += 1
        
            while have == need:
                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        
        left, right = res
        return s[left : right + 1] if res_len != float("inf") else ""
                
        