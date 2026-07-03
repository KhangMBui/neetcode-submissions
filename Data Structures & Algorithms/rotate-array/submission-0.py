class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        for _ in range(k):
            pop_num = nums.pop()
            nums.insert(0, pop_num)
        return nums
        