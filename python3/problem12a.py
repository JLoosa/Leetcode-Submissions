# Leetcode Problem 12
# Name: "Integer to Roman"
# Difficulty: Medium
# URL: https://leetcode.com/problems/integer-to-roman/
# Date: 2020-07-24
from collections import deque


# This is variation "a" or this program using a full lookup. View variation b for a better version
class Solution:

    def __init__(self):
        self.queue = deque()
        self.conversions = {
            0: {
                1: 'I',
                2: 'II',
                3: 'III',
                4: 'IV',
                5: 'V',
                6: 'VI',
                7: 'VII',
                8: 'VIII',
                9: 'IX',
            },
            1: {
                1: 'X',
                2: 'XX',
                3: 'XXX',
                4: 'XL',
                5: 'L',
                6: 'LX',
                7: 'LXX',
                8: 'LXXX',
                9: 'XC',
            },
            2: {
                1: 'C',
                2: 'CC',
                3: 'CCC',
                4: 'CD',
                5: 'D',
                6: 'DC',
                7: 'DCC',
                8: 'DCCC',
                9: 'CM',
            },
            3: {
                1: "M",
                2: "MM",
                3: "MMM"
            }
        }

    def intToRoman(self, num: int) -> str:
        place = -1
        while num > 0:
            place += 1
            place_value = num % 10
            num = num // 10
            if place_value == 0:
                continue
            representaion = self.get_representation(place, place_value)
            self.queue.appendleft(representaion)
        return "".join(self.queue)

    def get_representation(self, place, place_value):
        return self.conversions[place][place_value]
