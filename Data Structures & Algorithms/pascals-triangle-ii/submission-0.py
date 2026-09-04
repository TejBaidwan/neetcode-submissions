class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]

        prev = [1]

        for row in range(1, rowIndex + 1):
            current = [1] * (row + 1)

            for i in range(1, row):
                current[i] = prev[i - 1] + prev[i]

            prev = current

        return prev


        




        