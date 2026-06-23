class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Idea: prefix sum + hashmap
        # For each index, keep a running prefix sum: prefix_sum = sum(nums[0:i])
        # We want subarrays ending at current index whose sum is k

        # Hashmap with pair: (prefix sum : count)
        # so [2, -1, 1, 2], k = 2 would have a hashmap of:

        # First element: 2, currSum = 2. Check if currSum - k = 2 - 2 = 0 in Hashmap, yes
        # => res += 1. Hashmap: {0 : 1, 2 : 1}

        # Second element: -1, currSum = 1. Check if currSum - k = 1 - 2 = -1 in Hashmap, no.
        # {0 : 1, 1 : 1, 2 : 1}

        # Third element: 1, currSum = 2. Check if currSum - k = 2 - 2 = 0 in Hashmap. Yes => res += 1
        # {0 : 1, 1 : 1, 2 : 2}
        
        # Fourth element: 2, currSum = 4. Check if currSum - k = 4 - 2 = 2 in Hashmap. Yes => res += 2
        
        prefixSumCount = defaultdict(int)

        prefixSumCount[0] = 1

        res = currSum = 0

        for n in nums:
            currSum += n

            res += prefixSumCount[currSum - k]

            prefixSumCount[currSum] += 1
        return res