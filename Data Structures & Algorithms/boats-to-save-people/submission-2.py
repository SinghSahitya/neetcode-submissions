class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 1:
            return 1

        people.sort()

        boats = 0

        l = 0
        r = len(people) - 1
        while l < r:
            wgh = people[l] + people[r]
            if wgh > limit:
                boats += 1
                r -= 1
                if l == r:
                    boats += 1
                    break
            else:
                boats += 1
                l += 1
                r -= 1
                if l == r:
                    boats += 1
                    break

        return boats