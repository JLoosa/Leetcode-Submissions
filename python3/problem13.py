# Leetcode Problem 13
# Name: "Roman to Integer"
# Difficulty: Easy
# URL: https://leetcode.com/problems/integer-to-roman/
# Date: 2020-07-24

class Solution:

    # TODO: This method is very slow and inefficient. Revisit later
    def romanToInt(self, s: str) -> int:
        lookup = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        return sum(self.de_romanize(s, lookup))

    def de_romanize(self, roman: str, lookup: dict):
        keys = reversed(lookup.keys())
        for key in keys:
            while roman.startswith(key):
                roman = roman[len(key):]
                yield lookup[key]
