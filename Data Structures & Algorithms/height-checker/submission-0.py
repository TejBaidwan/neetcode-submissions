class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        frequency = {}
        count = 0

        for i in heights:
            frequency[i] = frequency.get(i, 0) + 1
        
        expected = sorted([key for key, count in frequency.items() for _ in range(count)])

        for i in range(len(expected)):
            if heights[i] != expected[i]:
                count += 1
        
        return count