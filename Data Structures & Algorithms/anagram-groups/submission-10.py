class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #solution: for each string, create a 
        #list of alphabet count
        #go over the list and if match, append
        ans = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] +=1
            ans[tuple(count)].append(s)
        return ans.values()

            
