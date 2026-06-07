class Solution:
    #solution: ["neet","code","love","you"] => 4#neet4#code4#love3#you
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        # Use l, r to iterate the string
        l = 0
        r = 1
        res = []
        while (r < len(s)):
            if (s[r] == '#'):
                length = int(s[l : r])
                # print(length)
                # print(s[r+1 : r + 1 + length])
                res.append(s[r + 1 : r + 1 + length])
                l = r + 1 + length
                r = l + 1
            else:
                r += 1
        return res