class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        # Iterate through s2 with the window size of len(s1)
        # while doing so, keeping track of current string's frequency map
        # if at any case, it = s1 frequency map => return True

        firstMap = Counter(s1)

        l, r = 0, len(s1)

        while r <= len(s2):
            secondMap = Counter(s2[l:r])
            if secondMap == firstMap:
                return True
            r += 1
            l += 1
        return False
        