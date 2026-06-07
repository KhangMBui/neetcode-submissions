class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        index_value_map = {}

        for index, value in enumerate(nums):
            if (target - value) in index_value_map:
                return [index_value_map.get(target - value), index]
            index_value_map[value] = index
        return []