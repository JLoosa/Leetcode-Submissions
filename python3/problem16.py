# Leetcode Problem 16
# Name: "3Sum Closest"
# Difficulty: Medium
# URL: https://leetcode.com/problems/3sum-closest/
# Date: 2020-07-24
from typing import List


class Solution:

    # Approach: Find the first number, then use a two-pointer scan like was done in problem 15
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        if length < 3:
            return []
        closest_value = None
        closest_dist = float('inf')
        # Subtract 2 because we still need b & c
        for a in range(length-2):
            last_a = nums[a]
            b = a + 1
            c = length-1
            while b < c:
                # The data is sorted, so if we are too low, we can increase our value by incrementing b.
                # Recall that c is at the end of the list and therefore the max value. This means that we
                # can only use it if we are too high and need to decrease the sum
                s = last_a + nums[b] + nums[c]
                if abs(s - target) < closest_dist:
                    closest_dist = abs(s-target)
                    closest_value = s
                if s < target:
                    b += 1
                elif s > target:
                    c -= 1
                else:
                    # Because we only need the closest value, we can just return if we have an exact match
                    return target
            # Scrubbing tool to prevent refinding solutions when "a" moves to the next index and the value is the same
            while a+2 < length and nums[a] == last_a:
                a += 1
        return closest_value


