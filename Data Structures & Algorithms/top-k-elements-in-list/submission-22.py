class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [2, 5, 5, 9, 9, 9], k = 2 => [5, 9]
        # { (2 : 1), (5: 2), (9 : 3)}
        # Somehow make it frequency retrievable and sorted
        # [1, 5, 9], index represents frequency
        # We then can traverse backward and get k elements
        if not nums or k < 0:
            return []
        # Initialize the frequency counting hashmap
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Convert it to an array
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        # now traverse backward and get k elements
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        