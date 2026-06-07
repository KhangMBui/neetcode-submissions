class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Solution: zip(position, speed) into a list and sort
        #in reverse to put the leading car on top
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = [] #contains timeToReach
        for p, s in pair:
            #Calculate timeToReach
            timeToReach = (target - p) / s
            if (stack and timeToReach <= stack[-1]):
                continue
            stack.append(timeToReach)
        return len(stack)