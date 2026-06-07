class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution: try to come up with a list of elements (list of numbers) with index being frequency
        count = {}
        # populate a hashmap of elements (number, frequency)
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        freq = [[] for n in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) == k):
                    return res
            