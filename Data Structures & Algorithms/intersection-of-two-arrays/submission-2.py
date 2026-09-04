class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = []

        for num in nums1:
            if num in result:
                continue
            else:
                if num in nums2:
                    result.append(num)
        
        return result