class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums)

        while l <= r:
            mid = l + (r - l) // 2

            count = 0
            for num in nums:
                if num >= mid:
                    count += 1

            if count == mid:
                return mid
            elif count > mid:
                l = mid + 1
            else:
                r = mid - 1

        return -1