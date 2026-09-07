class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        freq = {}

        for row in wall:
            position = 0

            for j in range(len(row)):
                position += row[j]

                if j != len(row) - 1:
                    freq[position] = freq.get(position, 0) + 1
        
        if not freq:
            return len(wall)
        return len(wall) - max(freq.values())

