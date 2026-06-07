class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #solution: 2 pointers start and end
        #sum of them > target, end --
        #sum of them < target, start ++
        l, r = 0, len(numbers) - 1
        while (l < r):
            curSum = numbers[l] + numbers[r]
            if (curSum > target): 
                r -= 1
            elif (curSum < target):
                l += 1
            else:
                return [l + 1, r + 1]