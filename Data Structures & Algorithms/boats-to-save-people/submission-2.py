class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if not people:
            return 0
        
        # Each boat carries at most 2 people at the same time
        # Each boat can carries up to 'limit' weight
        # people[i] is the weight
        # Return number of boats to carry every given person
        
        # Sort first? [5, 1, 4, 2] becomes [1, 2, 4, 5]
        # l, r pointers
        # if l + r == limit: l += 1, r -= 1, boat += 1
        # if l + r > limit: r -= 1, boat += 1
        # if l + r < limit: l += 1, keep current sum, do a while loop until
        # adding subsequent l to sum would exceed limit, then boat += 1

        # [1, 2, 2, 3, 3]; limit = 3 the 2 boats '3' have its own boats
        # [1, 2, 2], boats = 2
        # 1 + 2 = 3 => boats += 1 = 3
        # [2]
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0

        while l <= r:
            curr_weight = people[l] + people[r]
            if curr_weight <= limit:
                l += 1
                r -= 1
            elif curr_weight > limit:
                r -= 1
            boats += 1

        return boats