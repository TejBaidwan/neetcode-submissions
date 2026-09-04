class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        frequency = {}
        good_pairs = 0

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        for value in frequency.values():
            if value > 1:
                good_pairs += (value * (value - 1)) // 2
        
        return good_pairs