class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        total = 0
        left_max = 0
        right_max = 0

        while l < r:

            if height[l] <= height[r]:
                if height[l] > left_max:
                    left_max = height[l]
                else:
                    total += left_max - height[l]
                l += 1
            elif height[l] > height[r]:
                if height[r] > right_max:
                    right_max = height[r]
                else:
                    total += right_max - height[r]
                r -= 1

        return total 