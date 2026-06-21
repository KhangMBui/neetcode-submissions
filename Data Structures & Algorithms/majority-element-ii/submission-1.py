class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return -1
        
        nums.sort()

        current_number = nums[0]
        current_count = 0
        req = len(nums) / 3
        res = []

        for n in nums:
            if n != current_number:
                if current_count > req:
                    res.append(current_number)
                current_number, current_count = n, 0
            
            current_count += 1
        
        if current_count > req:
            res.append(current_number)

        return res