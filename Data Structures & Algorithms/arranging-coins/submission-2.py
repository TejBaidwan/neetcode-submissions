class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        l = 1
        r = n
        answer = 0

        while l <= r:
            mid = l + (r - l) // 2

            if (mid * (mid + 1)) // 2 <= n:
                answer = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return answer
        

