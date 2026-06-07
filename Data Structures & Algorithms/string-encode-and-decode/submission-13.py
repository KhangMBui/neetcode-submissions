class Solution:
    #Solution: ["neet","code","love","you"] => 4#neet4#code4#love3#you
    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr 
    def decode(self, s: str) -> List[str]:
        #Solution: use i and j to get integer
        result = []
        i = 0
        while i < len(s):
            j = i
            while (s[j] != '#'):
                j += 1
            #Once found #, we can get string length
            length = int(s[i : j])
            print(length)
            print(s[j + 1 : j + 1 + length])
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return result
