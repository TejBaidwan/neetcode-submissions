class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def at_most(target):
            if target < 0:
                return 0

            l = 0
            total = 0
            count = 0

            for r in range(len(nums)):
                total += nums[r]

                while total > target:
                    total -= nums[l]
                    l += 1

                count += r - l + 1

            return count

        return at_most(goal) - at_most(goal - 1)

