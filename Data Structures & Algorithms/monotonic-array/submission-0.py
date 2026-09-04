class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        condition = "Increasing" if nums[0] <= nums[1] else "Decreasing"
        
        for i in range(len(nums) - 1):
            if condition == "Increasing":
                if not nums[i] <= nums[i + 1]:
                    return False
            else:
                if not nums[i] >= nums[i + 1]:
                    return False
            
        return True