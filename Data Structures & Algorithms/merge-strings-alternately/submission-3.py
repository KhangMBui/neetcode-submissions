class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1 and not word2:
            return ""
        if not word1:
            return word2
        if not word2:
            return word1
        
        ptr_1, ptr_2 = 0, 0

        res = ""

        while ptr_1 < len(word1) and ptr_2 < len(word2):
            res += word1[ptr_1] + word2[ptr_2]
            ptr_1 += 1
            ptr_2 += 1
        
        if ptr_1 < len(word1):
            res += word1[ptr_1:]
        elif ptr_2 < len(word2):
            res += word2[ptr_2:]
        
        return res
