# Leetcode Problem 26
# Name: "Remove Duplicates from Sorted Array"
# Difficulty: Easy
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Date: 2020-07-25
from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        head = 0
        for x in range(1, len(nums)):
            if nums[x] > nums[head]:
                head += 1
                nums[head] = nums[x]
        return head + 1
