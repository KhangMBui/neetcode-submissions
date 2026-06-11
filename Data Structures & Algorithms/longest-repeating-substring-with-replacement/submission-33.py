class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # I'm thinking of using dictionary to keep track of 
        # character's frequency in the current string being iterated
        # Current substring's length - frequency of most-appeared char
        # Number of replacement = current substring's length - freq of mosta-appeared char
        # Once number of replacement exceeds k, we shrink the sliding window

        # XYYX, k = 2
        # l = 0, r = 0: {X : 1}
        # l = 0, r = 1: {X : 1, Y : 1}; current substring's length - freq = 0
        # l = 0, r = 2: {X : 1, Y : 2}; current substring's length - freq = 3 - 2 = 1
        # l = 0, r = 3: {X : 2, Y : 2}; current substring's length - freq = 4 - 2 = 2
        # return r - l + 1? = 4

        # AAABABB, k = 1
        # l = 0, r = 3: {A: 3, B : 1}; current substring's length - freq = 4 - 3 = 1
        # l = 0, r = 4: {A: 4, B : 1}; current substring's length - freq = 5 - 4 = 1
        # l = 0, r = 5: {A: 4, B : 2}; current substring's length - freq = 6 - 4 = 2 EXCEED
        # l = 1, r = 5: {A: 3, B : 2}: current substring's length - freq = 5 - 3 = 2 EXCEED
        # l = 2, r = 5: {A: 2, B : 2}: current substring's length - freq = 4 - 2 = 2 EXCEED
        # l = 3, r = 5: {A: 1, B : 2}: current substring's length - freq = 3 - 2 = 1
        # l = 3, r = 6: {A: 1, B : 3}: current substring's length - freq = 4 - 3 = 1
        # r - l + 1 = 4

        if not s:
            return 0
        
        l = 0
        res = 0
        char_freq = {}

        for r in range(len(s)):
            char_freq[s[r]] = char_freq.get(s[r], 0) + 1
            window_size = r - l + 1
            replacement_n = window_size - max(char_freq.values())
            if replacement_n > k:
                char_freq[s[l]] -= 1
                l += 1
            else:
                res = max(res, window_size)

        return res
