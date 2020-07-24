# Leetcode Problem 1
# Name: "Two Sum"
# Difficulty: Easy
# URL: https://leetcode.com/problems/two-sum/
# Date: 2020-07-24
from typing import List


class Solution:

    # Solution using nested loops
    def twoSum_A(self, nums: List[int], target: int) -> List[int]:
        num_count = len(nums)
        for x in range(num_count):
            for y in range(x, num_count):
                if nums[x] + nums[y] == target:
                    return [x, y]

    # Solution using list comprehension
    def twoSum_B(self, nums: List[int], target: int) -> List[int]:
        return [[x, y] for x in range(len(nums)) for y in range(x, len(nums)) if nums[x] + nums[y] == target][0]

    # Method called by the site
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.twoSum_B(nums, target)
