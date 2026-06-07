class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            # Make sure we don't use the repetitive value:
            if (i > 0 and a == nums[i - 1]):
                continue
            # Now that we found the first value, let's do two-sum
            l, r = i + 1, len(nums) - 1
            while (l < r):
                threeSum = a + nums[l] + nums[r]
                if (threeSum > 0):
                    r -= 1
                elif (threeSum < 0):
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]]);
                #Shift pointers by moving the left pointer:
                    l += 1
                    while (nums[l] == nums[l - 1] and l < r):
                        l+= 1
        return res
            