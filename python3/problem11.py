# Leetcode Problem 11
# Name: "Container With Most Water"
# Difficulty: Medium
# URL: https://leetcode.com/problems/container-with-most-water/
# Date: 2020-07-24
from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        max_area, left_bound, right_bound = 0, 0, len(height) - 1
        while left_bound < right_bound:
            area = (right_bound - left_bound) * min(height[left_bound], height[right_bound])
            if area > max_area:
                max_area = area
            if height[left_bound] < height[right_bound]:
                left_bound += 1
            else:
                right_bound -= 1
        return max_area
