class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution: Hashset of key as number and value as index
        hashmap = {}
        for i, a in enumerate(nums):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap.get(diff), i]
            hashmap[a] = i
        return []