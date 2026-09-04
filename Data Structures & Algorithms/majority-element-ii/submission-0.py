class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        freq = {}
        result = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, value in freq.items():
            if value > (len(nums) // 3):
                result.append(key)
        
        return result