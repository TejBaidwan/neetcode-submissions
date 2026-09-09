class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:

        l = min(
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1]
        )

        r = max(
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1]
        )

        while l < r:
            mid = l + (r - l) // 2
            count = 0

            for num1 in nums1:

                l2 = 0
                r2 = len(nums2)

                if num1 > 0:
                    while l2 < r2:
                        mid2 = l2 + (r2 - l2) // 2

                        if nums2[mid2] * num1 <= mid:
                            l2 = mid2 + 1
                        else:
                            r2 = mid2

                    count += l2

                elif num1 < 0:
                    while l2 < r2:
                        mid2 = l2 + (r2 - l2) // 2

                        if nums2[mid2] * num1 <= mid:
                            r2 = mid2
                        else:
                            l2 = mid2 + 1

                    count += len(nums2) - l2

                else:
                    if mid >= 0:
                        count += len(nums2)

            if count < k:
                l = mid + 1
            else:
                r = mid

        return l















