class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        frequency = {}
        max_lucky = -1

        for i in arr:
            frequency[i] = frequency.get(i, 0) + 1
        
        for key, value in frequency.items():
            if key == value:
                max_lucky = max(max_lucky, key)
        
        return max_lucky