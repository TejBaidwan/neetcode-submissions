class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        # [1, 2, 3, 3, 5, 6]
        
        nums.sort()
        l = 0
        min_difference = 10000000000000

        for r in range(len(nums)):
            if r - l + 1 == k:
                smallest = nums[l]
                largest = nums[r]

                if largest - smallest < min_difference:
                        min_difference = largest - smallest
            
                l += 1
        
        return min_difference

