class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Solution: zip (position, speed) into pairs
        #and sort pairs in reverse to put the leading car
        #to the front of the array
        stack = []
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(reverse = True)
        for p, s in pairs:
            timeToReach = (target - p) / s
            if not (stack and timeToReach <= stack[-1]):
                stack.append(timeToReach)
        return len(stack)