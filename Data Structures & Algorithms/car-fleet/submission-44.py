class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Solution: Create a list of pairs [p & s] from position and speed
        pairs = [[p, s] for p, s in zip(position, speed)]
        # Reverse sort it so the car at the 1st place is on top of the list
        pairs.sort(reverse = True)
        stack = []
        # Calculate timeToReach of each car and add it to the stack
        # if its time to reach is not faster than the first one of stack
        # The length of timeToReach is the result
        for p, s in pairs:
            timeToReach = (target - p) / s
            if (stack and timeToReach <= stack[-1]):
                continue
            stack.append(timeToReach)
        return len(stack)