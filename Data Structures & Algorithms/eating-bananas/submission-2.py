class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Return the minimum eating rate k
        # So basically we go from 1 -> onward
        # to find the hours where we could eat the banana within h (<= h)

        # Brute force solution: creates res = 1
        # iterate through the piles, at each index, digest everything at res ,
        # keep track of hours
        # until the end of the array, see if hours <= h, if not, keep going

        # The upper bound for k is max(piles). Because if Koko eats the largest
        # pile in 1 go (hour), she could do the same for the rest
        if not piles:
            return -1
  
        l, r = 1, max(piles)

        while l <= r:
            m = (r + l) // 2 # Let m be the current speed to test

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / m)
            
            if totalTime <= h:
                res = m
                # Keep finding smaller possible time, as we're looking for the min
                r = m - 1
            else:
                l = m + 1
        
        return res