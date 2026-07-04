class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Return k closest integers x in the array
        # Result should be sorted in ascending order

        # a is closer to b if:
        #   |a - x| < |b - x|
        #   |a - x| == |b - x| and a < b

        # [2, 4, 5, 8], k = 2, x = 4
        
        # Binary search to that position, and then in that position, use two 
        # pointers to look for the values?
        # Or simply do binary search and add numbers to it until list of numbers reaches k
        if not arr:
            return []

        n = len(arr)

        l, r = 0, n - 1

        while l < r:
            m = (l + r) // 2
            if arr[m] < x:
                l = m + 1
            else: # When equal, push leftward because smaller is more close
                r = m # do r = m because we're trying to find insertion position
        
        left, right = l - 1, l

        res = []

        while len(res) < k:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right >= n:
                res.append(arr[left])
                left -= 1
            elif abs(x - arr[left]) <= abs(x - arr[right]):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
        return sorted(res)
        
        
