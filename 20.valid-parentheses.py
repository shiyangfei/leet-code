#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (38.00%)
# Total Accepted:    842K
# Total Submissions: 2.2M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: "{[]}"
# Output: true
#
#
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        v_map = {
            '(': 0,
            '[': 0,
            '{': 0
        }
        match_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        v_list = []
        if s is None or s == '':
            return True
        for c in s:
            if v_map.get(c, None) is not None:
                v_list.append(c)
            elif match_map.get(c, None) is not None:
                expected_open_c = match_map.get(c)
                if len(v_list) == 0:
                    return False
                open_c = v_list.pop()
                if expected_open_c != open_c:
                    return False
            else:
                return False
        return len(v_list) == 0
