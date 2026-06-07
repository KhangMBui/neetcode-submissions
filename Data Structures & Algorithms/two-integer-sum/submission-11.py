class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if (diff in hashmap):
                return([hashmap.get(diff), i])
            hashmap[n] = i