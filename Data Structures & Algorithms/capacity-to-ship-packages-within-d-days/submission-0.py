class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l = max(weights)
        r = sum(weights)

        while l < r:
            mid = l + (r - l) // 2
            days_used = 1
            current = 0

            capacity = mid

            for weight in weights:
                if current + weight <= capacity:
                    current += weight
                else:
                    current = weight
                    days_used += 1
            
            if days_used > days:
                l = mid + 1
            elif days_used <= days:
                r = mid
        
        return l
            