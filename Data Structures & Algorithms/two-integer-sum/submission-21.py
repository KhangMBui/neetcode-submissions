class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution: Hashset of key as number and value as index
        hashset = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in hashset:
                return [hashset.get(remainder), i]
            hashset[nums[i]] = i
        return []