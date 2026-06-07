class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a stack of the final result:
        res = []
        # Create an array of pair, matches position and speed together.
        pair = [[p, s] for p, s in zip(position, speed)]
        # Sort it in reverse so we can get the fastest car at the top of the stack
        pair.sort(reverse = True)
        for p, s in pair:
            timeToReach = (target - p) / s
            if (res and timeToReach <= res[-1]):
                continue
            else:
                res.append(timeToReach)
        return len(res)