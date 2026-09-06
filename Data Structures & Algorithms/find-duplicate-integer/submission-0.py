class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums) - 1

        l = 1
        r = n

        while l < r:
            mid = l + (r - l) // 2

            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                r = mid
            else:
                l = mid + 1
        
        return l


            