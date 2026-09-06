class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1

        volume = 0

        left_max = height[l]
        right_max = height[r]

        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max > right_max:
                r -= 1
            elif left_max < right_max:
                l += 1
            else:
                l += 1

            if left_max > height[l]:
                volume += left_max - height[l]
            elif height[r] < right_max:
                volume += right_max - height[r]
        
        return volume


            
            

            
