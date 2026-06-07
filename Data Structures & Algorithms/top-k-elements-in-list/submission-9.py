class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution: create a list of (frequency - [list of number with that freq])
        # Create the frequency matrix with same length with the nums list:
        freq = [[] for i in range(len(nums) + 1)]
        # Create the count hashMap to keep track of number - freq
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # Put it into freq:
        for n, c in count.items():
            freq[c].append(n)
        # Now iterate backward the freq matrix and get number until enough
        res = []
        for i in range(len(freq) - 1, - 1, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) == k):
                    return res
        
