class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        # Iterate through s2 with the window size of len(s1)
        # while doing so, keeping track of current string's frequency map
        # if at any case, it = s1 frequency map => return True

        l, r = 0, len(s1)
        firstMap = Counter(s1)
        secondMap = Counter(s2[l:r])

        if firstMap == secondMap:
            return True

        while r < len(s2):
            if secondMap == firstMap:
                return True
            
            secondMap[s2[l]] -= 1

            if secondMap[s2[l]] == 0:
                del secondMap[s2[l]]
            
            secondMap[s2[r]] += 1

            r += 1
            l += 1
            if secondMap == firstMap:
                return True
        return False
        