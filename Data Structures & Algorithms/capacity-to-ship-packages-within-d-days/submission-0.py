class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # We must distribute the weights into loads to be shipped through out given days
        # It's like we must find a minimum subarray, but we don't have a fixed window size
        # But how do we...partition the weights for the days?

        def can_ship(capacity):
            """
            decide if a given capacity c
            """
            days_needed = 1
            curr_load = 0
            for weight in weights:
                if curr_load + weight > capacity:
                    days_needed += 1
                    curr_load = 0

                curr_load += weight
            return days_needed <= days


        # smallest weight capacity must be max(weights)
        # biggest weight capacity could be sum(weights), because easiest case is ship
        # everything in 1 day
        l, r = max(weights), sum(weights)
        res = 0
        # We're trying to find the minimum workable capacity across n days
        while l <= r:
            m = (r + l) // 2 # A candidate capacity

            # Check if this capacity could work
            if can_ship(m):
                res = m
                r = m - 1 # Look backwards for even smaller capacity
            else:
                l = m + 1
        return res