class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #solution, create a list of list of frequency that goes
        #frequency - number
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        #initialize the count hashMap with number - its freq:
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        #now put it to the freq at the position of the frequency
        for n, c in count.items():
            freq[c].append(n)
        res = []
        # now we iterate backward and put number in freq to res
        # until reached desired length
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) == k):
                    return res
