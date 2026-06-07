class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Check if s1 is in s2
        if len(s1) > len(s2):
            return False
        # Solution: Use two ascii alphabetical array
        # and a sliding window of size s1, iterate through
        # s2 and check if each window matches the array in s1
        countS1, countS2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1
        for i in range(len(s1), len(s2)):
            if countS1 == countS2:
                return True
            countS2[ord(s2[i]) - ord('a')] += 1
            countS2[ord(s2[i - len(s1)]) - ord('a')] -= 1
        return countS1 == countS2