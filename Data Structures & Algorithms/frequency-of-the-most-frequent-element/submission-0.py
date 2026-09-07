class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        l = 0
        total = 0
        max_freq = 0

        for i in range(len(nums)):
            total += nums[i]

            operations_needed = (nums[i] * (i - l + 1)) - total

            while operations_needed > k:
                total -= nums[l]
                l += 1

                operations_needed = (nums[i] * (i - l + 1)) - total

            max_freq = max(max_freq, i - l + 1)
        
        return max_freq

        
        
            
                