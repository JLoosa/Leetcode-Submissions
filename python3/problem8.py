# Leetcode Problem 8
# Name: "String to Integer (atoi)"
# Difficulty: Medium
# URL: https://leetcode.com/problems/string-to-integer-atoi/
# Date: 2020-07-24


class Solution:

    def myAtoi(self, str_in: str) -> int:
        if not str_in:
            return 0
        str_in = str_in.split(" ")
        for s in str_in:
            if s:
                try:
                    for i in range(len(s)):
                        if i == 0 and (s[i] == '-' or s[i] == '+'):
                            continue
                        try:
                            int(s[i])
                        except:
                            s = s[0:i]
                            break
                    val = int(s)
                    if val >= 2**31:
                        return 2**31-1
                    if val < -(2**31):
                        return -(2**31)
                    return val

                except:
                    return 0
        else:
            return 0
