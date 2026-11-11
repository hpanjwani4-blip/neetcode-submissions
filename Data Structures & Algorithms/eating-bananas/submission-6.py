import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)
        k=upper
        max_hours = h
        while lower <= upper:
            total_hour = 0
            mid = (lower + upper)//2
            for pile in piles:
                total_hour = total_hour + math.ceil(pile/mid)

            print(upper, lower, mid, total_hour)
            
            if total_hour > h:
                lower = mid + 1
            
            if total_hour <= h:
                k = mid
                upper = mid-1

        return k


        