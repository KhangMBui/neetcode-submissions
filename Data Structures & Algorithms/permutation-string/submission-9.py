class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Solution: Create a list of 26 zeros.
        # Use the length of the first string as the window size to slide
        if (len(s1) > len(s2)):
            return False
        # Initialize the alphabet list of character frequency
        countS1, countS2 = [0] * 26, [0] *26
        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1
        # Basically now we have iterated the first iteration 
        # of the sliding window
        for i in range(len(s1), len(s2)):
            if (countS1 == countS2):
                return True
            countS2[ord(s2[i]) - ord('a')] += 1
            countS2[ord(s2[i - len(s1)]) - ord('a')] -= 1
        return countS1 == countS2