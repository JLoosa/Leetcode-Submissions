# Leetcode Problem 10
# Name: "Regular Expression Matching"
# Difficulty: Hard
# URL: https://leetcode.com/problems/regular-expression-matching/
# Date: 2020-07-24


# TODO: Reattempt at a later point. The implementation does not work.
class Solution:

    def __init__(self):
        self.s_index = 0
        self.s_len = 0
        self.p_index = 0
        self.p_len = 0
        self.is_asterisked = False
        # (Letter, Asterisked)
        self.last_match = (None, False)

    def rearrange_pattern(self, p: str) -> str:
        p_list = list(a for a in p)
        for i in range(len(p_list)):
            if p_list[i] == '*':
                last_char = p_list[i-1]
                if i + 1 < self.p_len:
                    next_char = p_list[i+1]
                    if next_char == last_char:
                        p_list[i] = next_char
                        p_list[i+1] = "*"
        return "".join(p_list)

    def isMatch(self, s: str, p: str) -> bool:

        self.s_index = 0
        self.s_len = len(s)

        self.p_index = -1
        self.p_len = len(p)

        print("Pattern is:", p)
        p = self.rearrange_pattern(p)
        print("Pattern is now:", p)

        self.is_asterisked = False

        def next_p():
            self.p_index += 1
            if self.is_asterisked:
                self.p_index += 1

            self.is_asterisked = self.p_index + 1 < self.p_len and p[self.p_index+1] == '*'

        next_p()

        while self.s_index < self.s_len:
            if self.p_index >= self.p_len:
                # We hit the end of our pattern before the end of your word.
                return False
            target = p[self.p_index]
            s_let = s[self.s_index]

            print("Comparing:", (target, s_let))
            if target == '.' or target == s_let:
                print("Match")
                # This is a match
                self.last_match = (s_let, self.is_asterisked)
                self.s_index += 1
                if not self.is_asterisked:
                    next_p()
            elif self.is_asterisked:
                print("End Asterisk")
                next_p()
            else:
                print("Fail")
                return False
        # We are at the end of the string, let's ensure that we do not have any other non-asterisked pattern inputs
        while self.p_index < self.p_len:
            if not self.is_asterisked:
                l, a = self.last_match
                if not a or (l != p[self.p_index]):
                    print("Non-Asterisked Target:", p[self.p_index])
                    return False
            next_p()
        return True
