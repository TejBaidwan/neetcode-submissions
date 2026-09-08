class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        r = 0

        answer = len(nums) + 1
        total = 0

        while r < len(nums):
            total += nums[r]
            r += 1

            while total >= target:
                answer = min(answer, r - l)
                total -= nums[l]
                l += 1

        if answer == len(nums) + 1:
            return 0

        return answer
