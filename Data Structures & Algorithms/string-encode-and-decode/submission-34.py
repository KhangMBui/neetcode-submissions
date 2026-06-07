class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        print("Encoded:", encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        i = j = 0
        res = []

        while j < len(s):
            while (s[j] != '#'):
                j += 1
            strLength = int(s[i : j])
            res.append(s[j + 1 : j + 1 + strLength])
            i = j + 1 + strLength
            j = i

        return res

        
