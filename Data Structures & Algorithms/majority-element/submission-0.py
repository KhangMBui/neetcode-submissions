class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        num_count = Counter(nums)
        n = len(nums)
        req = n / 2


        for num, count in num_count.items():
            if count > req:
                return num
        return -1