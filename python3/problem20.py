# Leetcode Problem 20
# Name: "Valid Parentheses"
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-parentheses/
# Date: 2020-07-24

# The general approach for this is likely to be a stack. I will implement this using a list
class Stack:

    def __init__(self):
        self.stack = list()

    def push(self, char: str):
        self.stack.append(char)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return not self.stack



class Solution:

    def isValid(self, s: str) -> bool:
        stack = Stack()
        push_values = {'(':')', '[':']', '{':'}'}
        for letter in s:
            if letter in push_values:
                stack.push(push_values[letter])
            else:
                if stack.is_empty() or letter != stack.pop():
                    return False
        return stack.is_empty()


