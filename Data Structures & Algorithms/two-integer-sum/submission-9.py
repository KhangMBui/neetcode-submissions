class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #solution: create a hashMap (value - index) and go over the list
        #find the diff of the target and the current number
        #if cool we can return the i and the hashMapget(diff)
        hashMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if (diff in hashMap):
                return [hashMap.get(diff), i]
            else:
                hashMap[nums[i]] = i