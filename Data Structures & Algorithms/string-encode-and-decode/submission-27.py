class Solution:
    # Solution: 4#neet4#code4#love3#you
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded
    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        res = []
        while (j < len(s)):
            while (s[j] != '#'):
                j += 1
            strLength = int(s[i:j])
            res.append(s[j + 1: j + strLength + 1])
            j = j + strLength + 1
            i = j
        return res