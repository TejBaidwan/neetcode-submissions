class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0
        flowerbed_imaginary = [0] + flowerbed + [0]

        for flower in range(len(flowerbed)):
            i = flower + 1

            if (flowerbed_imaginary[i] == 0 and
                flowerbed_imaginary[i - 1] == 0 and
                flowerbed_imaginary[i + 1] == 0):

                flowerbed_imaginary[i] = 1
                count += 1

        return count >= n
