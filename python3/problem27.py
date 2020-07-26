# Leetcode Problem 27
# Name: "Remove Element"
# Difficulty: Easy
# URL: https://leetcode.com/problems/remove-element/
# Date: 2020-07-25
from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        head = 0
        for x in range(0, len(nums)):
            if nums[x] != val:
                nums[head] = nums[x]
                head += 1
        return head
