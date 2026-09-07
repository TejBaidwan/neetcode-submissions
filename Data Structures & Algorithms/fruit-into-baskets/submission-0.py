class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        total = 0
        freq = {}

        l = 0

        for i in range(len(fruits)):
            freq[fruits[i]] = freq.get(fruits[i], 0) + 1

            while len(freq) > 2:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                l += 1
        
            total = max(total, i - l + 1)
        
        return total

