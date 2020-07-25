# Leetcode Problem 1
# Name: "Two Sum"
# Difficulty: Easy
# URL: https://leetcode.com/problems/two-sum/
# Date: 2020-07-24
from typing import List


class Solution:

    # Solution using a binary search approach
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        # We need to keep the original as the algorithm is meant to work on unsorted data
        sorted_list = sorted(nums)
        for a in range(length-1):
            s_t = target - nums[a]
            if self.binary_search(sorted_list, s_t):
                try:
                    # We do the search from a+1 because we don't want to let a be used twice
                    b = nums.index(s_t, a+1)
                    return [a, b]
                except ValueError:
                    continue

    # Returns true if the target is in the provided list
    # False other wise
    def binary_search(self, sorted_list: List[int], target: int) -> bool:
        lo, hi = 0, len(sorted_list) -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if sorted_list[mid] == target:
                return True
            elif sorted_list[mid] < target:
                lo = mid+1
            else:
                hi = mid-1
        return False
