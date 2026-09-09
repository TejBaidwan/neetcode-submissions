class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        l = max(nums)
        r = sum(nums)
        parts = 0
        total = 0

        while l <= r:
            total = 0
            parts = 1
            mid = l + (r - l) // 2

            for num in nums:
                if total + num > mid:
                    parts += 1
                    total = num
                else:
                    total += num
            
            if parts <= k:
                r = mid - 1
            else:
                l = mid + 1
        
        return l

