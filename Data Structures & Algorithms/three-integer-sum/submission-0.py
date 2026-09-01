class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sorted_list = sorted(nums)

        l = 1
        r = len(nums) - 1
        output = []

        for i in range(len(sorted_list) - 2):
            l = i + 1
            r = len(sorted_list) - 1

            while l < r:
                total = sorted_list[i] + sorted_list[l] + sorted_list[r]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    triplet = [sorted_list[i], sorted_list[l], sorted_list[r]]

                    if triplet not in output:
                        output.append(triplet)

                    l += 1
                    r -= 1
        
        return output


