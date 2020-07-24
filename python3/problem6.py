# Leetcode Problem 6
# Name: "ZigZag Conversion"
# Difficulty: Medium
# URL: https://leetcode.com/problems/zigzag-conversion/
# Date: 2020-07-24


class Solution:

    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s
        delta = 1
        row = 0
        lists = [[] for _ in range(num_rows)]
        for letter in s:
            lists[row].append(letter)
            if row == 0:
                delta = 1
            if row == num_rows - 1:
                delta = -1
            row += delta

        return "".join(letter for sublist in lists for letter in sublist)
