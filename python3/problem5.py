# Leetcode Problem 5
# Name: "Longest Palindromic Substring"
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-palindromic-substring/
# Date: 2020-07-24


class Solution:

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        longest = ""
        for start in range(length):
            letter = s[start]
            for end in range(start + len(longest), length):
                if s[end] != letter:
                    continue
                s1 = s[start:end + 1]
                if s1 == s1[::-1]:
                    longest = s1
        return longest
