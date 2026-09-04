class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)

        a = sorted_nums[-1]
        b = sorted_nums[-2]
        c = sorted_nums[0]
        d = sorted_nums[1]

        return (a * b) - (c * d)