# Leetcode Problem 4
# Name: "Median of Two Sorted Arrays"
# Difficulty: Hard
# URL: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Date: 2020-07-24
from typing import List


class Solution:

    def median(self, lst: List[int]) -> float:
        length = len(lst)
        mid = int(length/2)
        if length % 2:
            return lst[mid]
        else:
            return (lst[mid-1] + lst[mid])/2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # TODO: Time complexity is in excess of O(log(n+m). Revisit this problem in the future
        return self.median(sorted(nums1 + nums2))

