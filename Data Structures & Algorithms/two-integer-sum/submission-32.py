class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        
        hashmap = {}

        for i, a in enumerate(nums):
            diff = target - a
            if diff in hashmap:
                return [hashmap.get(diff), i]
            hashmap[a] = i
        return []