# Leetcode Problem 4
# Name: "Median of Two Sorted Arrays"
# Difficulty: Hard
# URL: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Date: 2020-07-24
from typing import List


class Solution:

    def median(self, lst: List[int]) -> float:
        # Time complexity should not exceed O(log (n+m)), so this method only works if python has an O(1) implementation for len() on a list
        # Fortunately, the Python wiki claims that it does: https://wiki.python.org/moin/TimeComplexity
        length = len(lst)
        mid = int(length/2)
        if length % 2:
            return sum(lst[mid:mid+1])/2
        else:
            return lst[mid]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return (self.median(nums1) + self.median(nums2))/2

