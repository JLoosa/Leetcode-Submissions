# Leetcode Problem 2
# Name: "Add Two Numbers"
# Difficulty: Medium
# URL: https://leetcode.com/problems/add-two-numbers/
# Date: 2020-07-24

from math import log10


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def to_number(self, list_node: ListNode) -> int:
        offset = 1
        val = 0
        while list_node:
            val += list_node.val * offset
            offset *= 10
            list_node = list_node.next
        return val

    def to_list(self, number: int) -> ListNode:
        if not number:
            return ListNode(0)
        node = None
        exp_raw = log10(number)
        exp = int(exp_raw)
        while exp >= 0:
            power = 10**exp
            cur = ListNode(int(number/power))
            number = number % power
            if node:
                cur.next = node
            node = cur
            exp -= 1
            if exp < 0:
                break
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number1 = self.to_number(l1)
        number2 = self.to_number(l2)
        total = number1 + number2
        return self.to_list(total)
