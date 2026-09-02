class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        result = [0] * len(nums)

        l = 0
        r = len(nums) - 1

        for pos in range(len(nums) - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                result[pos] = nums[l] ** 2
                l += 1
            else:
                result[pos] = nums[r] ** 2
                r -= 1

        return result
            
        
        