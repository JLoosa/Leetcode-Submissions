# Leetcode Problem 25
# Name: "Reverse Nodes in k-Group"
# Difficulty: Hard
# URL: https://leetcode.com/problems/reverse-nodes-in-k-group/
# Date: 2020-07-25
from typing import List

from python3 import ListNode


# This is the same as what we had in the previous question, just with a different section to reverse
class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
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
        nodes = [n for n in self.iterate_list(nodes, k)]
        # Reassign the next values
        for x in range(1, length):
            nodes[x-1].next = nodes[x]
        # Clear the end to stop cycles
        nodes[len(nodes)-1].next = None
        return nodes[0]

    # Generator to walk the function. It uses two for loops. One to find the end of each reversed section,
    # and the other to walk backwards to yield the value in reverse at those sections
    def iterate_list(self, nodes: List[ListNode], k: int):
        if not nodes or len(nodes) == 1:
            yield nodes
        if k == 1:
            for nodes in nodes:
                yield nodes
        if k > 1:
            length = len(nodes)
            x1 = 0
            # Start at k-1 so that we get the 0th element
            for x in range(k-1, length, k):
                x1 = x
                for i in range(x, x-k, -1):
                    yield nodes[i]
            # This loop is to make sure we don't miss any values
            while x1 + 1 < length:
                x1 += 1
                yield nodes[x1]
