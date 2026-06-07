class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        #solution: zip (position, speed) in pairs of the stack
        #and sort them in reverse to put the leading car to the
        #first position:
        pairs = [[p, s] for p,s in zip(position, speed)]
        pairs.sort(reverse = True)
        for p, s in pairs:
            timeToReach = (target - p) / s
            #stack will hold timeToReach of every car
            if (stack and timeToReach <= stack[-1]):
                continue
            else:
                stack.append(timeToReach)
        return len(stack)
