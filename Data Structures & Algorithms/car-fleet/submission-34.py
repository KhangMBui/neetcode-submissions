class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Solution: zip them in pair of (position, speed)
        #and then sort it in reverse so that the 1st place car
        #is put in front
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        print(pair)
        stack = [] #get this as a timeToReach stack 
        #we need to get their timeToReach = (target - position) / speed
        for p, s in pair:
            timeToReach = (target - p) / s
            print(timeToReach)
            if not (stack and timeToReach <= stack[-1]):
                stack.append(timeToReach)
        return len(stack)