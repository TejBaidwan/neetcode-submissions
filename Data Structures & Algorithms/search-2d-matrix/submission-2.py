class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in matrix:
            l = 0
            r = len(i) - 1
            while l <= r:
                midpoint = l + (r - l) // 2

                if i[midpoint] < target:
                    l = midpoint + 1
                elif i[midpoint] > target:
                    r = midpoint - 1
                else:
                    return True
        
        return False
