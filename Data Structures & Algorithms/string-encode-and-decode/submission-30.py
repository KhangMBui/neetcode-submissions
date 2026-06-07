class Solution:
    # Solution: "4#neet4#code4#love3#you"
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while (s[i] != '#'):
                i += 1
            strLength = int(s[j : i])
            res.append(s[i + 1 : i + 1 + strLength])
            i += 1 + strLength
        return res