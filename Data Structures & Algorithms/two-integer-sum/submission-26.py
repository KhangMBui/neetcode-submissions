class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach: hashmap approach? { (number, index)}
        # [3, 4, 5, 6] => { (3 : 0), (4 : 1), (5 : 2), (6 : 3) }
        # Iterate through the array, take target substract by the current
        # num, we'd get the number we're looking for. We then 
        # look for that number in hashmap and potentially retrieve the index

        if not nums:
            return []
        hashmap = {}
        for i, n in enumerate(nums):
            remainder = target - n
            if remainder in hashmap:
                return [hashmap[remainder], i]
            hashmap[n] = i
        return []
            
        