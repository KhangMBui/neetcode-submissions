class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # match the pair of position and speed together in a list
        pair = [[p, s] for p, s in zip(position, speed)]
        #Reverse sort so the biggest position (leader) is the one up top
        pair.sort(reverse = True)
        #Stack to keep track of time to reach of each car
        stack = []
        for p, s in pair:
            timeToReach = (target - p) / s
            stack.append(timeToReach)
            if (len(stack) > 1 and stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)