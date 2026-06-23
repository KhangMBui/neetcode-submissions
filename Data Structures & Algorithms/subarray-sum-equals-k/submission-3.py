class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # First element: 2, currSum = 2. Check if currSum - k = 2 - 2 = 0 in Hashmap, yes
        # => res += 1. Hashmap: {0 : 1, 2 : 1}

        # Second element: -1, currSum = 1. Check if currSum - k = 1 - 2 = -1 in Hashmap, no.
        # {0 : 1, 1 : 1, 2 : 1}

        # Third element: 1, currSum = 2. Check if currSum - k = 2 - 2 = 0 in Hashmap. Yes => res += 1
        # {0 : 1, 1 : 1, 2 : 2}
        
        # Fourth element: 2, currSum = 4. Check if currSum - k = 4 - 2 = 2 in Hashmap. Yes => res += 2

        # We'll keep a hashmap of count of running prefix_sum. 
        # The (key : value) pair is (prefix sum : count)
        # Iterate through the number, at each number, we check if the prefix Sum before it + current number = k
        # If yes, that's a subarray that suffices the requirement. There may also be many subarray before that suffice this
        # requirement.
        # So we check if prefix_sum - k exists in our hashmap count, and how many times? We add that to the running res
        
        prefixSumCount = defaultdict(int)

        prefixSumCount[0] = 1

        res = currSum = 0

        for n in nums:
            currSum += n

            res += prefixSumCount[currSum - k]

            prefixSumCount[currSum] += 1
        return res