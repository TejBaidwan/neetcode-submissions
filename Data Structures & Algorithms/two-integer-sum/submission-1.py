class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        collection = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in collection:
                return [collection[complement], index]
            
            collection[num] = index
        

        