class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hash map of value - index
        hashMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if (diff in hashMap):
                return [hashMap.get(diff), i]
            hashMap[n] = i
        