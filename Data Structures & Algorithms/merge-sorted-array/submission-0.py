class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Solution: Have 3 pointers: p1 for nums1, p2 for nums2, and
        # and one 'last' to keep track of the last index in the iteration backward
        # Approach: iterate backwared of both nums, and comparing and adding number to the last pointer

        # [1, 2, 10, 20, 20, 40]
        # [1, 2] 
        p1 = m - 1
        p2 = n - 1
        last = m + n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[last] = nums1[p1]
                p1 -= 1
                last -= 1
            else:
                nums1[last] = nums2[p2]
                p2 -= 1
                last -= 1
        
        print("Current nums1: ", nums1)

        