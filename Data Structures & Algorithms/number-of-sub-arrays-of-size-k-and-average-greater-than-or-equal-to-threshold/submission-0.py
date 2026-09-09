class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        l = 0

        count = 0

        for r in range(len(arr)):
            if r - l + 1 == k:
                window_sum = sum(arr[l:r + 1])
                average = window_sum / k

                if average >= threshold:
                    count += 1
                
                l += 1
        
        return count