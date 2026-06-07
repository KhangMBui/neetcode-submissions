class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Solution: create a pair that matches position to speed
        pair = [[p,s] for p, s in zip(position, speed)]
        #sort in reverse
        pair.sort(reverse = True)
        stack = []
        for p, s in pair:
            speedToReach = (target - p) / s
            stack.append(speedToReach)
            if (len(stack) >= 2 and stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)

        