class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # The four number needs to be within 0 and n, n is len(nums)
        # a, b, c, d are 4 different numbers
        # The four numbers need to add up to target

        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            # Avoids duplicate:
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                # Avoids duplicate
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                l, r = j + 1, n - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
        return res
        