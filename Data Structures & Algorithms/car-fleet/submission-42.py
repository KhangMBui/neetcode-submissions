class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # solution: zip (position, speed) into a stack
        # and sort it in reverse to the 1st place car is 
        # first place in the stack
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(reverse = True)
        # res stack stores timeToReach of each car,
        # determining the number of car left 
        stack = []
        for p, s in pairs:
            timeToReach = ( target - p ) / s
            if (stack and timeToReach <= stack[-1]):
                continue
            stack.append(timeToReach)
        return len(stack)