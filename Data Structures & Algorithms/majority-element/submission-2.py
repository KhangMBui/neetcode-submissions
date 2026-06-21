class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        # Boyer-Moore Voting Algorithm
        # Maintain a candidate and a count
        # whenever see a candidate, increment count. 
        # Otherwise, decrement it.
        # When count reaches 0, we pick a new candidate
        # [5, 5, 1, 1, 1, 5, 5]
        # At first, res = 5
        # 5 and 5: count = 2
        # 1: count - 1 = 1
        # 1: count - 1 = 0 => now res = 1
        # 1: count + 1 = 1
        # 5: count - 1 = 0 => now res = 5
        # 5: count + 1 = 1 => return 5

        res = count = 0

        for n in nums:
            if count == 0:
                res = n
            if n == res:
                count += 1
            else:
                count -= 1
        return res