class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #solution: create a list of [list of numbers], indexed by its frequency
        #firstly, initialize the hashmap of [number, frequency]
        hashMap = {}
        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)
        #now reverse it 
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in hashMap.items():
            freq[c].append(n)
        #now we traverse the freq list in reverse and get numbers until reached k
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) == k):
                    return res