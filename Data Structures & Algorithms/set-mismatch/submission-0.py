class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        nums_set = set(nums)
        expected = set()
        nums_freq = {}
        difference = []

        for num in nums:
            nums_freq[num] = nums_freq.get(num, 0) + 1

        for i in range(len(nums)):
            expected.add(i + 1)   

        for key, value in nums_freq.items():
            if value > 1:
                difference.append(key)   
        
        difference.extend(list(expected - nums_set))

        return difference