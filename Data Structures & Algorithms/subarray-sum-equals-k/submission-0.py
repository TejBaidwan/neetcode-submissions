class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        count = 0
        sum = 0
        frequency = {0: 1}

        for num in nums:
            sum += num

            if sum - k in frequency:
                count += frequency[sum - k]

            frequency[sum] = frequency.get(sum, 0) + 1

        return count

