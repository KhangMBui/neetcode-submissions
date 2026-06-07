class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Solution: zip (position,speed) into pairs and sort
        # them in reverse so the first place car is at the front of stack
        pairs = [[p, s] for p,s in zip(position, speed)]
        pairs.sort(reverse = True)
        stack = []
        for p, s in pairs:
            timeToReach = (target - p) / s
            if stack and timeToReach <= stack[-1]:
                continue
            else:
                stack.append(timeToReach)
        return len(stack)