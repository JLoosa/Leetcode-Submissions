# Leetcode Problem 12
# Name: "Integer to Roman"
# Difficulty: Medium
# URL: https://leetcode.com/problems/integer-to-roman/
# Date: 2020-07-24


# This is variation "b" or this program using a partial lookup
class Solution:


    def intToRoman(self, num: int) -> str:
        lookup = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        return "".join(self.romanize(num, lookup))

    def romanize(self, num: int, lookup: dict):
        keys = sorted(lookup.keys(), reverse=True)
        while num > 0:
            for key in keys:
                yield (num // key) * lookup[key]
                num %= key
