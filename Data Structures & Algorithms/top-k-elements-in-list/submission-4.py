class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #solution: we need a hashmap of pair: number - frequency
        #and a list of frequency - number
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        #initialize the hashmap with each number and their frequencies
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        #now put them into the freq list in the reverse order of pair
        for n, c in count.items():
            freq[c].append(n)
        #Now look for result by iterate the freq list backward until reach k
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) == k):
                    return res

