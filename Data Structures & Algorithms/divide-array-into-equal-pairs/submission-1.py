class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        if len(nums) % 2 != 0:
            return False
        
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        for value in frequency.values():
            if value % 2 != 0:
                return False
        
        return True