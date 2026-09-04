class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        smallest = float('inf')
        second_smallest = float('inf')
        largest = float('-inf')
        second_largest = float('-inf')

        for num in nums:
            if num <= smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest:
                second_smallest = num

            if num >= largest:
                second_largest = largest
                largest = num
            elif num > second_largest:
                second_largest = num

        return (largest * second_largest) - (smallest * second_smallest)