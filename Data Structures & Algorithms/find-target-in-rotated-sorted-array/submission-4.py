class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        midpoint = 0

        while l <= r:
            midpoint = l + (r - l) // 2

            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] >= nums[l]:
                if nums[l] <= target < nums[midpoint]:
                    r = midpoint - 1
                else:
                    l = midpoint + 1
            elif nums[midpoint] <= nums[r]:
                if nums[midpoint] < target <= nums[r]:
                    l = midpoint + 1
                else:
                    r = midpoint - 1
        
        return -1
        