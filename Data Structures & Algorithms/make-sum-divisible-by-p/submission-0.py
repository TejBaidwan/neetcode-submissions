class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        total = 0

        for num in nums:
            total += num

        target = total % p

        if target == 0:
            return 0

        sum = 0
        remainder_index = {0: -1}
        min_length = len(nums)

        for i, num in enumerate(nums):
            sum += num
            curr_remainder = sum % p

            needed = (curr_remainder - target) % p

            if needed in remainder_index:
                min_length = min(min_length, i - remainder_index[needed])

            remainder_index[curr_remainder] = i

        return min_length if min_length < len(nums) else -1
