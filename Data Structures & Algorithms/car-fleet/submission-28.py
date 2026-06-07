class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #zip them together as a stack of pair (position - speed)
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        res = []
        for p, s in pair:
            timeToReach = (target - p) / s
            res.append(timeToReach)
            if (len(res) >= 2 and res[-1] <= res[-2]):
                res.pop()
        return len(res)