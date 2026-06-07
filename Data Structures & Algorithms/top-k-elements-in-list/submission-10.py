class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Create a list that goes backward
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        #initialize the count hashmap (number : count):
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        #now put it into freq, reverse the value into (count : [list of number]):
        for n, c in count.items():
            freq[c].append(n)
        res = []
        #now iterate backward to get result until reach desired amount:
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) ==  k):
                    return res