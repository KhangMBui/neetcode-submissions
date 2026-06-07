class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Create frequency counts for s1 and the first window of s2
        countS1 = [0] * 26
        countS2 = [0] * 26

        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1

        # Sliding window to compare frequency counts
        for i in range(len(s1), len(s2)):
            if countS1 == countS2:
                return True
            # Slide the window: include the next character and remove the first one
            countS2[ord(s2[i]) - ord('a')] += 1
            countS2[ord(s2[i - len(s1)]) - ord('a')] -= 1

        # Check the last window
        return countS1 == countS2
