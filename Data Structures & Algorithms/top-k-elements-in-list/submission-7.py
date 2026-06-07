class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution: create a reverse array of array of number of (frequency - [numbers])
        freq = [[] for i in range(len(nums) + 1)]
        # A (number - count) hashmap:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # now put it into freq:
        for n, c in count.items():
            freq[c].append(n)
        # Result array:
        res = []
        # Reverse iteration and get number until enough:
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) == k):
                    return res