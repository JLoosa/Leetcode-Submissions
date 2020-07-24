# Leetcode Problem 9
# Name: "Palindrome Number"
# Difficulty: Easy
# URL: https://leetcode.com/problems/palindrome-number/
# Date: 2020-07-24


class Solution:

    # Solution without converting to a string
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # Ensure we are in the domain of log
        if x == 0:
            return True
        rev = self.int_reverse(x)
        return rev == x

    def int_reverse(self, x: int) -> int:
        if x < 10:
            return x
        count = 1
        num = 0
        while x > 0:
            num = (num * 10) + (x % 10)
            x = x // 10
        return num

