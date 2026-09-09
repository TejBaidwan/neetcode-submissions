class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        l = 0
        count = 0
        window_sum = 0

        for r in range(len(arr)):
            window_sum += arr[r]

            if r - l + 1 == k:
                average = window_sum / k

                if average >= threshold:
                    count += 1

                window_sum -= arr[l]
                l += 1

        return count
