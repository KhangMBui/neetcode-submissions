class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return -1
        
        num_count = Counter(nums)
        n = len(nums)
        req = n / 3
        res = []


        for num, count in num_count.items():
            if count > req:
                res.append(num)
        return res