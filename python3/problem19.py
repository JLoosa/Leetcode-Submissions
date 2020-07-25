# Leetcode Problem 19
# Name: "Remove Nth Node From End of List"
# Difficulty: Medium
# URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Date: 2020-07-24

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Complexity is O(n)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Find the length
        tmp = head
        length = 0
        while tmp is not None:
            length += 1
            tmp = tmp.next
        # Remove the node
        tmp, prev = head, None
        for _ in range(length - n):
            prev = tmp
            tmp = tmp.next
        if prev is None:
            # We must be at the head
            return tmp.next
        else:
            prev.next = tmp.next
        return head

