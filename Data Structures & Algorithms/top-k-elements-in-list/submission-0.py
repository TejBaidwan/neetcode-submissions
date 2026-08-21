from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for number, frequency in count.items():
            buckets[frequency].append(number)
        
        output = []
        for frequency in range(len(nums), 0, -1):
            output.extend(buckets[frequency])
            if len(output) >= k:
                return output[:k]
            