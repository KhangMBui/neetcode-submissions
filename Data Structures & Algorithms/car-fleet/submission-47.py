class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Solution: Create a pair of (position, speed) sorted
        # in reverse order so the first place car is at the front
        # of the pair
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(reverse = True)
        stack = []
        for p, s in pairs:
            timeToReach = (target - p) / s
            if (stack and timeToReach <= stack[-1]):
                continue
            stack.append(timeToReach)
        return len(stack)