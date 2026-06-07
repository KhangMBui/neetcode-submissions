class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashMap = {}
        stack = []
        for p, s in zip(position, speed):
            hashMap[p] = s
        hashMap = {p : s for p, s in sorted(hashMap.items(), reverse=True)}
        for p, s in hashMap.items():
            timeToReach = ( target - p ) / s
            stack.append(timeToReach)
            if (len(stack) > 1 and stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)

        