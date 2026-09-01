class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l <= r:

            rate = l + (r - l) // 2

            hours = 0

            for pile in piles:
                hours += - (-pile // rate)
            
            if hours > h:
                l = rate + 1
            else:
                r = rate - 1
        
        return l