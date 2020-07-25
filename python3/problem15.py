# Leetcode Problem 15
# Name: "3Sum"
# Difficulty: Medium
# URL: https://leetcode.com/problems/3sum/
# Date: 2020-07-24
from typing import List


class Solution:

    # Approach: Find the first number, then use a two-pointer scan like was done in problem 11
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        length = len(nums)
        if length < 3:
            return []
        valid = set()
        # Subtract 2 because we still need b & c
        for a in range(length-2):
            last_a = nums[a]
            b = a + 1
            c = length-1
            s = -1
            while b < c:
                # The data is sorted, so if we are too low, we can increase our value by incrementing b.
                # Recall that c is at the end of the list and therefore the max value. This means that we
                # can only use it if we are too high and need to decrease the sum
                s = last_a + nums[b] + nums[c]
                if s < 0:
                    b += 1
                elif s > 0:
                    c -= 1
                else:
                    valid.add((last_a, nums[b], nums[c]))
                    b += 1
            # Scrubbing tool to prevent refinding solutions when "a" moves to the next index and the value is the same
            while a+2 < length and nums[a] == last_a:
                a += 1
        return [list(x) for x in valid]


