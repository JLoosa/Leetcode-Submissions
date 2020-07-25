# Leetcode Problem 22
# Name: "Generate Parentheses"
# Difficulty: Medium
# URL: https://leetcode.com/problems/generate-parentheses/
# Date: 2020-07-25
from typing import List

# This problem is very amusing to be because it feels a lot like partitions.
# That said, this is actually a simple grammar with the following definition
# S -> <P> | (<P>)<P> | ε
# P -> ()


# To generate these recursively, we can use the following function
def generate_s(n: int):
    # Base Cased
    if n <= 0:
        yield ""
    for x in range(n):
        for left in generate_s(x):
            for right in generate_s(n-1-x):
                yield "({}){}".format(left, right)


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        return [_ for _ in generate_s(n)]

