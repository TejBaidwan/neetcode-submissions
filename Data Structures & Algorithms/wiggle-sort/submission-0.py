class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)):

            if i == len(nums) - 1:
                return nums

            elif i % 2 == 0:
                if nums[i] <= nums[i + 1]:
                    continue
                else:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] >= nums[i + 1]:
                    continue
                else:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        
        return nums

        