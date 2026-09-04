class Solution:
    def scoreOfString(self, s: str) -> int:
        
        sum = 0

        for i in range(len(s) - 1):
            abs_difference = abs(ord(s[i]) - ord(s[i + 1]))
            sum += abs_difference
        
        return sum