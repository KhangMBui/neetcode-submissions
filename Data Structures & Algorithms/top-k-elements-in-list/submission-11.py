class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Solutions: create an array that goes frequency-list of number
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        #Initialize the hashmap:
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        #now initialize the freq matrix:
        for n, c in count.items():
            freq[c].append(n)
        res = []
        #now iterate freq backward and get number until reaching k
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) == k):
                    return res