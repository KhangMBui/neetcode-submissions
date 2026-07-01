class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge sort

        def merge(arr, left, mid, right):
            left_arr, right_arr = arr[left : mid + 1], arr[mid + 1 : right + 1]
            i, j, k = left, 0, 0

            while j < len(left_arr) and k < len(right_arr):
                if left_arr[j] <= right_arr[k]:
                    arr[i] = left_arr[j]
                    j += 1
                else:
                    arr[i] = right_arr[k]
                    k += 1
                i += 1
            
            while j < len(left_arr):
                arr[i] = left_arr[j]
                j += 1
                i += 1

            while k < len(right_arr):
                arr[i] = right_arr[k]
                k += 1
                i += 1
        
        def mergeSort(arr, left, right):
            if left < right:
                mid = (left + right) // 2

                mergeSort(arr, left, mid)
                mergeSort(arr, mid + 1, right)
                merge(arr, left, mid, right)
        
        mergeSort(nums, 0, len(nums) - 1)
        return nums