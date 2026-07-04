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

        idx = 0
        n = len(arr)

        for i in range(n):
            if abs(x - arr[i]) < abs(x - arr[idx]):
                idx = i
        
        res = [arr[idx]]
        l, r = idx - 1, idx + 1

        while len(res) < k:
            if l >= 0 and r < n:
                if abs(x - arr[l]) <= abs(x - arr[r]):
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            elif l >= 0:
                res.append(arr[l])
                l -= 1
            elif r < n:
                res.append(arr[r])
                r += 1
        return sorted(res)