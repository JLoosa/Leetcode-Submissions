# Leetcode Problem 28
# Name: "Implement strStr()"
# Difficulty: Easy
# URL: https://leetcode.com/problems/implement-strstr/
# Date: 2020-07-25

class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        h_len = len(haystack)
        n_len = len(needle)
        if n_len > h_len:
            return -1
        for x in range(h_len - n_len + 1):
            if haystack[x] != needle[0]:
                continue
            if haystack[x:x+n_len] == needle[:]:
                return x
        return -1
