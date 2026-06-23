class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Idea: prefix sum + hashmap
        # For each index, keep a running prefix sum: prefix_sum = sum(nums[0:i])
        # We want subarrays ending at current index whose sum is k
        # [2, -1, -1, 2]
        # {2 : 1, }

        # We'll create a hashmap that keeps on going sum
        # We'll iterate through nums, on each number at index i,
        # we'll see if (k - current number) exists in the hashmap
        # If yes => add 1 to res

        # Hashmap with pair: (prefix sum : count)
        # so [2, -1, -1, 2], k = 2 would have a hashmap of:
        # {0 : 2, 2 : 2, 1 : 1}
        
        prefixSumCount = defaultdict(int)
        prefixSumCount[0] = 1

        res = 0
        currSum = 0

        for n in nums:
            currSum += n
            
            res += prefixSumCount[currSum - k]

            prefixSumCount[currSum] += 1

        return res