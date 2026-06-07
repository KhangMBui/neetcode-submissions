class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #solution: a list of [list of numbers], indexed by its frequency
        #firstly, initialize a hashmap of number - count
        count  = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        #now create the freq list of list
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        #now traverse the freq in reverse and get number until reach k
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) == k):
                    return res