class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Solution: zip them together as a list of pair (position - speed):
        pair = [[p, s] for p, s in zip(position, speed)]
        #sort in reverse to bring the car with the closest
        #position to the goal to the front
        pair.sort(reverse = True) 
        stack = []
        for p, s in pair:
            timeToReach = (target - p) / s
            if (stack and stack[-1] >= timeToReach):
                continue
            else:
                stack.append(timeToReach)
        return len(stack)