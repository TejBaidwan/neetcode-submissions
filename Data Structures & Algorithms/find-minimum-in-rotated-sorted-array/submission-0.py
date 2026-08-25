class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        while l < r:
            midpoint = l + (r - l) // 2
            if nums[midpoint] > nums[r]:
                l = midpoint + 1
            else:
                r = midpoint
        
        return nums[l]