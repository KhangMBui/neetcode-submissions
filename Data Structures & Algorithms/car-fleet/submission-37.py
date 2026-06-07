class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        #Solution: zip (position, speed) into a stack of pair
        pair = [[p, s] for p, s in zip(position, speed)]
        #sort it in reverse so that the leading car be at the front
        pair.sort(reverse = True)
        #Solution: get a time to reach destination of each car
        #and compare
        for p, s in pair:
            timeToReach = (target - p) / s
            if not (stack and timeToReach <= stack[-1]):
                stack.append(timeToReach)
        return len(stack)
