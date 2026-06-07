class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # value - index
        for i, n in enumerate(nums):
            diff = target - n
            if (diff in hashMap):
                return [hashMap.get(diff), i]
            hashMap[n] = i