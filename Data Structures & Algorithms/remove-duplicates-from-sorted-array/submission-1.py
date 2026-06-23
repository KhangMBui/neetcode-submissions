class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        unique = set()
        l = 0

        for r in range(len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]  
  
            unique.add(nums[r])
        return len(unique)