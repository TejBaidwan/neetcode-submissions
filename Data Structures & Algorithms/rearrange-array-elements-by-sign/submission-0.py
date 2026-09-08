class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        result = [0] * len(nums)

        positive = 0
        negative = 1

        for i in range(len(nums)):
            if nums[i] > 0:
                result[positive] = nums[i]
                positive += 2
            else:
                result[negative] = nums[i]
                negative += 2
        
        return result

        