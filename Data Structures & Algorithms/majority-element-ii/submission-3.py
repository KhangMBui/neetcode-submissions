class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return -1
        
        # Boyer-Moore Voting Algorithm
        num1, cnt1 = 0, 0
        num2, cnt2 = 0, 0

        for n in nums:
            if n == num1:
                cnt1 += 1
            elif n == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = n
                cnt1 = 1
            elif cnt2 == 0:
                num2 = n
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        # Found 2 majority elements, now count their occurrences
        cnt1 = cnt2 = 0
        for n in nums:
            if n == num1:
                cnt1 += 1
            elif n == num2:
                cnt2 += 1
        
        res = []
        req = len(nums) / 3
        # Add candidates with count greater than n/3 to the result
        if cnt1 > req: 
            res.append(num1)
        if cnt2 > req:
            res.append(num2)
        return res
