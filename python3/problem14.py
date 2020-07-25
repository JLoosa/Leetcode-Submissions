# Leetcode Problem 14
# Name: "Longest Common Prefix"
# Difficulty: Easy
# URL: https://leetcode.com/problems/longest-common-prefix/
# Date: 2020-07-24
from typing import List


class Solution:

    def longestCommonPrefix(self, all_strings: List[str]) -> str:
        prefix = ""
        if not all_strings:
            return prefix
        end_length = min(len(s) for s in all_strings)
        done = False
        for x in range(end_length):
            if done:
                break
            tmp = all_strings[0][x]
            for s in all_strings:
                if s[x] != tmp:
                    done = True
                    break
            else:
                prefix += s[x]
        return prefix
