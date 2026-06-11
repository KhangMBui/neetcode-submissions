class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        # Iterate through s2 with the window size of len(s1)
        # while doing so, keeping track of current string's frequency map
        # if at any case, it = s1 frequency map => return True

        firstMap = Counter(s1)
        secondMap = Counter(s2[0:len(s1)])

        if firstMap == secondMap:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            secondMap[s2[r]] += 1

            secondMap[s2[l]] -= 1
            if secondMap[s2[l]] == 0:
                del secondMap[s2[l]]
            
            if secondMap == firstMap:
                return True
            
            r += 1; l+= 1
        
        return False
        