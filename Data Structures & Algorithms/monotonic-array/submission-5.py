class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        condition = ""
        index = 0

        while True:

            if len(nums) <= 2:
                return True
            elif nums[index] > nums[index + 1]:
                condition = "Decreasing"
                break
            elif nums[index] < nums[index + 1]:
                condition = "Increasing"
                break
            else:
                index += 1
            
            if index == len(nums) - 1:
                return True
        
        for i in range(len(nums) - 1):
            if condition == "Increasing":
                if not nums[i] <= nums[i + 1]:
                    return False
            else:
                if not nums[i] >= nums[i + 1]:
                    return False
            
        return True