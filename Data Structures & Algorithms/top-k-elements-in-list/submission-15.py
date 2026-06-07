class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #solution: a list of [list of numbers], indexed by its frequency
        count = {}
        # Initialize the dictionary of (number, its frequency)
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if (k == len(res)):
                    return res
        