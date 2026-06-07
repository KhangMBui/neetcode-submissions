class Solution:
    # Solution: 4#Neet4#Code4#love3#you
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
    def decode(self, s: str) -> List[str]:
        # Create two iterator i & j to get length of work
        # when reach #
        result = []
        i = 0
        while (i < len(s)):
            j = i
            while (s[j] != '#'):
                j += 1
            wordLength = int(s[i : j])
            result.append(s[j + 1 : j + 1 + wordLength])
            i = j + 1 + wordLength
        return result