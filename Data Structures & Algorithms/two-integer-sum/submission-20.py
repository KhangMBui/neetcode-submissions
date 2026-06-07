class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution: Hashmap (key: number - value: index)
        # Iterate through all numbers in nums
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if (diff in hashmap):
                return [hashmap[diff], i]
            hashmap[n] = i
        return []