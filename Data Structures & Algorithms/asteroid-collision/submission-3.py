class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # For aesteroids[i], abs val = size
        # sign = its direction (positive = right, negative = left)
        # speed of all are the same
        
        # Find out the state of the aesteroids after all collisions
        # If 2 aesteroids meet, smaller one explode
        # Same size -> both explore
        # aesreoid moving in the same direction will never meet

        # [2, 4, -4, -1]
        # [->, ->, <-, <-]

        stack = []

        for a in asteroids:
            alive = True
            while alive and a < 0 and (stack and stack[-1] > 0):
                if abs(stack[-1]) < abs(a):
                    stack.pop()
                elif abs(stack[-1]) > abs(a):
                    alive = False
                    break
                else:
                    stack.pop()
                    alive = False
                    break
            if alive:
                stack.append(a)
        return stack
