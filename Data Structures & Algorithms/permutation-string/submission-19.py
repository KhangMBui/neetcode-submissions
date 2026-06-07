class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        # Solution: use the ascii alphabet list to control s1 and s2
        countS1 = [0]*26
        countS2 = [0]*26
        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1
        # Iterate through s2 in range of countS1's length
        for i in range(len(s1), len(s2)):
            if (countS1 == countS2):
                return True
            countS2[ord(s2[i]) - ord('a')] += 1
            countS2[ord(s2[i - len(s1)]) - ord('a')] -= 1
        return countS1 == countS2