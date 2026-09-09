class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        l = 0

        minimum = float('inf')
        white = 0
        black = 0

        for r in range(len(blocks)):
            if blocks[r] == 'W':
                white += 1
            else:
                black += 1
            
            if r - l + 1 == k:
                steps = k - black
                minimum = min(minimum, steps)

                if blocks[l] == 'W':
                    white -= 1
                else:
                    black -= 1
                
                l += 1
        
        return minimum
