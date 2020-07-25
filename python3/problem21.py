# Leetcode Problem 21
# Name: "Merge Two Sorted Lists"
# Difficulty: Easy
# URL: https://leetcode.com/problems/merge-two-sorted-lists/
# Date: 2020-07-24
from python3 import ListNode


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        out_head, out_tail = None, None
        while l1 or l2:
            if not l1:
                if out_tail:
                    out_tail.next = l2
                    return out_head
                else:
                    return l2
            if not l2:
                if out_tail:
                    out_tail.next = l1
                    return out_head
                else:
                    return l1
            if l1.val < l2.val:
                next = l1
                l1 = l1.next
            else:
                next = l2
                l2 = l2.next
            if not out_head:
                out_head = next
            else:
                out_tail.next = next
            out_tail = next
        return out_head
