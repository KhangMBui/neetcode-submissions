class Solution:
    # Solution : ["neet", "code", "love", "you"] -> 4#neet4#code4#love4#you
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result +=  str(len(s)) + "#"  + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        l = 0
        r = 1
        while ( r < len(s) ):
            if (s[r] == '#'):
                strLength = int(s[l : r])
                result.append(s[r + 1 : r + 1 + strLength])
                l = r + 1 + strLength
                r = r + 2 + strLength
            else:
                r += 1
        return result
