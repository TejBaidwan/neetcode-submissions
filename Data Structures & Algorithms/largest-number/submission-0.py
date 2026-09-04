class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = [str(num) for num in nums]

        for i in range(len(nums)):
            best = i

            for j in range(i + 1, len(nums)):
                if nums[j] + nums[best] > nums[best] + nums[j]:
                    best = j

            nums[i], nums[best] = nums[best], nums[i]

        result = "".join(nums)

        return "0" if result[0] == "0" else result
