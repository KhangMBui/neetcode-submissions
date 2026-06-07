class Solution:
    #solution: 4#neet4#code4#love3#you
    def encode(self, strs: List[str]) -> str:
        encoded = "";
        for s in strs:
            encoded += str(len(s)) + "#" + s
        print(encoded)
        return encoded
    def decode(self, s: str) -> List[str]:
        res = []
        #create i and j to do it
        i = 0
        while (i < len(s)):
            j = i
            while (s[j] != '#'):
                j += 1
            strLength = int(s[i : j])
            res.append(s[j + 1 : j + 1 + strLength])
            i = j + 1 + strLength
        print(res)
        return res
            