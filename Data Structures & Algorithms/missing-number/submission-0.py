class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        freq = {}
        expected = []

        for i in range(len(nums) + 1):
            expected.append(i)

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for expect in expected:
            if expect not in freq:
                return expect
