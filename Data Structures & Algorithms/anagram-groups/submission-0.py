class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list) #mapping charCount to list of Anagrams
        for s in strs:
           count = [0] * 26 #a...z
           for c in s:
                count[ord(c) - ord('a')] +=1
           #In python, List cannot be keys, so we have to do tuple(List)
           ans[tuple(count)].append(s)
        return ans.values()
           
            
