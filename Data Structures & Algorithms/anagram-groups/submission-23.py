class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution: Dictionary of ([alphabetic array], [list of strings])
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values()