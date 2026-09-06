class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_freq = sorted(freq.items(), key=lambda item: (item[1], -item[0]))

        result = []

        for num, count in sorted_freq:
            result.extend([num] * count)

        return result

