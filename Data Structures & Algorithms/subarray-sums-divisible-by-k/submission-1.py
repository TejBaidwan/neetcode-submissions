class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        sum = 0
        modulos = []
        freq = {0: 1}
        total = 0

        for num in nums:
            sum += num
            modulos.append(sum % k)
        
        for modulo in modulos:
            freq[modulo] = freq.get(modulo, 0) + 1
        
        for key, value in freq.items():
            total += (value * (value - 1)) // 2
        
        return total

        