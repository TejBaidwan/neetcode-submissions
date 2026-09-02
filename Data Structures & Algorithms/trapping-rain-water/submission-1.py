class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        total_area = 0
        left_max = height[l]
        right_max = height[r]

        while l < r:

            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max < right_max:
                total_area += left_max - height[l]
                l += 1
            else:
                total_area += right_max - height[r]
                r -= 1
        
        return total_area
            


            
            

            
