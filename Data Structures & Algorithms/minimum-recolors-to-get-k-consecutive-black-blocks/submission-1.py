class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        l = 0

        minimum = float('inf')
        black = 0

        for r in range(len(blocks)):
            if blocks[r] == 'B':
                black += 1
            
            if r - l + 1 == k:
                steps = k - black
                minimum = min(minimum, steps)

                if blocks[l] == 'B':
                    black -= 1
                
                l += 1
        
        return minimum
