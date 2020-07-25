# Leetcode Problem 23
# Name: "Merge k Sorted Lists"
# Difficulty: Hard
# URL: https://leetcode.com/problems/merge-k-sorted-lists/
# Date: 2020-07-25
from typing import List

from python3 import ListNode


# My opinion on this problem is that it is a lot like a SumK problem where an efficient implementation of Sum2 is the answer.
# To solve this, I will use a modified version of my method problem 21 (Merge 2 sorted lists), and repeatedly apply it
# Assuming the Big-O of my merge2 is O(n) where n is the length of the longest list, the runtime of this will be O(kn), where
# k is the number of lists
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            if not l1:
                return l2
            if not l2:
                return l1
            out_head, out_tail = None, None
            while l1 or l2:
                if not l1:
                    out_tail.next = l2
                    return out_head
                if not l2:
                    out_tail.next = l1
                    return out_head
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

        out = mergeTwoLists(lists[0], lists[1])
        for x in range(2, len(lists)):
            out = mergeTwoLists(out, lists[x])
        return out
