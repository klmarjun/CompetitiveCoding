import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = nums1 + nums2
        lst.sort()
        return (lst[len(lst)//2-1] + lst[len(lst)//2])/2 if len(lst)%2 == 0 else lst[len(lst)//2]
