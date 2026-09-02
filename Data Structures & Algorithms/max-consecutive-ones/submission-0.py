class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    
        total = 0
        streak = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                streak += 1
                total = max(total, streak)
            else:
                streak = 0

        return total

