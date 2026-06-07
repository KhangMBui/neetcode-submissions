class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution: we need array of number in the index of frequency
        # For example: [1, 2, 2, 3, 3, 4, 5, 5, 5]
        # => [[1, 4], [2, 3], [5]]
        # Then we iterate backward and get element until reach k
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        freq = [[] for n in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res