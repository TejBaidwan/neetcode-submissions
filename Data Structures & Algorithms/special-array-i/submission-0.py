class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        
        l = 0
        r = 1

        for i in range(len(nums) - 1):
            if nums[l] % 2 != nums[r] % 2:
                l += 1
                r += 1
            else:
                return False
        
        return True