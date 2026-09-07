class Solution:
    def minSwaps(self, s: str) -> int:
        
        l = 0

        swaps = 0
        balance = 0

        swaps = 0
        balance = 0

        for i in range(len(s)):
            if s[i] == '[':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                swaps += 1
                balance = 1

        return swaps

