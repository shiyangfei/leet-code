#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses
#
# Easy (33.22%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"["'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" are all valid
# but "(]" and "([)]" are not.
# 
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        symbol_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        pipe = []
        for index, c in enumerate(s):
            if c in symbol_map:
                if len(pipe) == 0:
                    return False
                if pipe[-1] != symbol_map[c]:
                    return False
                pipe = pipe[:-1]
            else:
                pipe.append(c)
        return len(pipe) == 0
