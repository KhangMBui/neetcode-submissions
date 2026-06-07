class Solution:
    # Solution : ["neet", "code", "love", "you"] -> 4#neet4#code4#love4#you
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result +=  str(len(s)) + "#"  + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while (i < len(s)):
            j = i
            while (s[j] != '#'):
                j += 1
            strLen = int(s[i : j])
            result.append(s[j + 1 : j + 1 + strLen])
            i = j + 1 + strLen
        return result
