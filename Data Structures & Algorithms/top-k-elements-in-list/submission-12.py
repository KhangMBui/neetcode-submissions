class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution: create a list of list that goes: (frequency - [list of numbers])
        count = {}
        # initialize (number - freq) hashmap:
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        freq = [ [] for i in range(len(nums) + 1)]
        # Now put it in reverse pair order in freq:
        for n, c in count.items():
            freq[c].append(n)
        result = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                result.append(n)
                if (len(result) == k):
                    return result
        