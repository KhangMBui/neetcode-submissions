class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Result: use a dictionary ([alphabetic array], [list of strings corresponding to the alphabetic array])
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values()