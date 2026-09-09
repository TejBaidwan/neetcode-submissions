class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        l = 0
        r = 0
        freq = {}
        count = 0
        prefix_count = 0

        while r < len(nums):
            freq[nums[r]] = freq.get(nums[r], 0) + 1

            if len(freq) > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
                prefix_count = 0

            while freq[nums[l]] > 1:
                freq[nums[l]] -= 1
                l += 1
                prefix_count += 1

            if len(freq) == k:
                count += prefix_count + 1

            r += 1

        return count
