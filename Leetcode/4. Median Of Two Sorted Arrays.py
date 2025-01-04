class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = nums1 + nums2
        sorted_res = sorted(res)
        n = len(sorted_res)
        if n % 2 == 0:
            median = (sorted_res[n // 2 - 1] + sorted_res[n // 2]) / 2
        else:
            median = sorted_res[n // 2]
        return median
