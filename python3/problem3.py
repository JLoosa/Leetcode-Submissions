# Leetcode Problem 3
# Name: "Longest Substring Without Repeating Characters"
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Date: 2020-07-24


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        history = list()
        max_length = 0
        length = 0
        for letter in s:
            while letter in history:
                del history[0]
                length -= 1
            history.append(letter)
            length += 1
            if length > max_length:
                max_length = length
        return max_length
