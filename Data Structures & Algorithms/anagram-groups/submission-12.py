class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # solutions: for each string in the list, create
        # a count array of character and match them
        ans = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


            
