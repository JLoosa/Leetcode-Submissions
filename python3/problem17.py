# Leetcode Problem 17
# Name: "Letter Combinations of a Phone Number"
# Difficulty: Medium
# URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Date: 2020-07-24
from typing import List


class Solution:

    # This is a permutations problem where the program needs to generate every possibility.
    # The number of possibilities will be equal to the product of the lengths of the strings in the lookup
    def letterCombinations(self, digits: str) -> List[str]:
        lookup = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        digits = digits.replace("1", "").replace("0", "")
        if not digits:
            return list()
        return [x for x in self.get_combination(digits, lookup)]

    # Doing this recursively with generator functions. It's fairly quick but uses a good bit of memory
    def get_combination(self, s: str, d: dict):
        key = s[0]
        for letter in d[key]:
            if len(s) > 1:
                yield letter + self.get_combination(s[1:], d)
            else:
                yield letter



