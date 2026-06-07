class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hash map count (item: number, key: count)
        # create an array of array (matrix) called freq
        # this freq array will contains element of most frequently appeared,
        # going up
        count = {} #number - count
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            #Put item - key into hashmap:
            count[n] = 1 + count.get(n, 0)
        #Now add those to freq, with its value at the position that equals to
        #its frequency
        for n, c in count.items():
            freq[c].append(n)
        res = []
        #Iterate backward 
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) == k):
                    return res
        