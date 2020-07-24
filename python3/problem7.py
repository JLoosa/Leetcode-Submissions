# Leetcode Problem 7
# Name: "Reverse Integer"
# Difficulty: Easy
# URL: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Date: 2020-07-24


class Solution:


    def reverse(self, x: int) -> int:
        if x > 0:
            rev = int(str(x)[::-1])
        else:
            rev = -int(str(abs(x))[::-1])
        max_num = (2**31)
        if rev not in range (-max_num, max_num):
            return 0
        return rev
