class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # The idea: the array is rorated, cut into 2 sorted halves
        # So we find the point where it got cut
        # And then we could perform 2 binary searches in the 2 halves
        # to find the position

        # But then what if it was rotated len(nums) times?
        # which means it will go back to normal. 
        # So I'm thinking...we'll create a function to 
        # do binary search.

        # Step 1: Loop through array to find the cut point
        #   If no cut point, simply search whole array
        # Step 2: Split the array into 2 arrays, and
        #   perform binary search on first half. If not found,
        #   perform binary search on the second half.

        # Edge case:
        if not nums:
            return -1
        
        def binary_search(l: int, r: int) -> int:
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
            return -1
        
        # Find cut point:
        curr_value = nums[0]
        cut_index = -1

        for i in range(1, len(nums)):
            if nums[i] < curr_value:
                cut_index = i
                break
            curr_value = nums[i]
        
        # If not cut point, simply search whole array:
        if cut_index == -1:
            print("No cut point")
            return binary_search(0, len(nums) - 1)

        print("Cut index: ", cut_index)
        
        # Split into 2 arrays
        first_start, first_end = 0, cut_index - 1
        second_start, second_end = cut_index, len(nums) - 1

        first_result = binary_search(first_start, first_end)
        
        return first_result if first_result != -1 else binary_search(second_start, second_end)


        