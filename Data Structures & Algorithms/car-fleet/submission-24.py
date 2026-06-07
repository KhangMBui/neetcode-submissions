class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        for p, s in pair:
            timeToReach = (target - p) / s
            if (res and timeToReach <= res[-1]):
                continue
            else:
                res.append(timeToReach)
        return len(res)