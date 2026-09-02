class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        greatest = arr[-1]

        for i in range(-2, -(len(arr)) - 1, -1):
            curr = arr[i]
            arr[i] = greatest

            if curr > greatest:
                greatest = curr

        arr[-1] = -1

        return arr

