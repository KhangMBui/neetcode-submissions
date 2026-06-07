class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution: make a list of frequency - [list of numbers]
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # flip the dict:
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        # Now iterate it backward
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) == k):
                    return res