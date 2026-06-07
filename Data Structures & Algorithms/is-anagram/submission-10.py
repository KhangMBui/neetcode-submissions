class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #solution: create two counting hashmap
        #and go over one string, put those character into the hashmap
        #finally compare the hashmaps
        if (len(s) != len(t)):
            return False
        countT, countS = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        