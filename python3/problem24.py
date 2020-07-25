# Leetcode Problem 24
# Name: "Swap Nodes in Pairs"
# Difficulty: Medium
# URL: https://leetcode.com/problems/swap-nodes-in-pairs/
# Date: 2020-07-25
from python3 import ListNode


class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        # Make sure we have input that would allow switching
        if not head or not head.next:
            return head
        # Add them all to a list
        nodes = list()
        while head:
            nodes.append(head)
            head = head.next
        length = len(nodes)
        # Rearrange them
        for x in range(length):
            if x % 2:
                tmp = nodes[x-1]
                nodes[x-1] = nodes[x]
                nodes[x] = tmp
        # Reassign the next values
        for x in range(1, length):
            nodes[x-1].next = nodes[x]
        # Clear the end to stop cycles
        nodes[len(nodes)-1].next = None
        return nodes[0]




