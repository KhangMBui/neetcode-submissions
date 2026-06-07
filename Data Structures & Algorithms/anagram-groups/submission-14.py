class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution: for each string, create a count array of 26*0
        # and fill in number of characters
        ans = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()