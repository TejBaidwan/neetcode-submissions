class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        collection = set(nums)
        longest = 0

        for num in collection:
            if num - 1 not in collection:
                current = num

                while current in collection:
                    current += 1

                longest = max(longest, current - num)

        return longest
