class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        sum = 0
        count = 0
        even = 1
        odd = 0

        for num in arr:
            sum += num

            if sum % 2 == 0:
                count += odd
                even += 1
            else:
                count += even
                odd += 1
        
        return count


