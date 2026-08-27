class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l = 0
        r = len(nums1)

        while l <= r:
            midpoint = l + (r - l) // 2

            partition1 = midpoint
            partition2 = (len(nums1) + len(nums2) + 1) // 2 - partition1

            left1 = nums1[partition1 - 1] if partition1 > 0 else float("-inf")
            right1 = nums1[partition1] if partition1 < len(nums1) else float("inf")

            left2 = nums2[partition2 - 1] if partition2 > 0 else float("-inf")
            right2 = nums2[partition2] if partition2 < len(nums2) else float("inf")


            if left1 <= right2 and left2 <= right1:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                r = partition1 - 1
            
            elif left2 > right1:
                l = partition1 + 1



            


        
