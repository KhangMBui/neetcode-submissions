class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # solution: map list position and list speed into a list of pair [position, speed]
        # sort it in reverse
        # iterate it and find each car time to reach the destination, push it to the stack
        # if length of stack is at least 2, and time of the latest car is 
        # less than time of the car below it in the stack, we pop() the latest car
        # simply bc we a car can't pass
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []
        for p, s in pair:
            stack.append( (target - p) / s )
            if (len(stack) > 1 and stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)

        