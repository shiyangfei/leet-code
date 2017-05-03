#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses
#
# Easy (32.94%)
# Total Accepted:    192525
# Total Submissions: 584383
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
        length = len(s)
        index = 0
        while index < length:
            c = s[index]
            if is_open(c):
                if index == length - 1:
                    return False
            else:
                if index == 0:
                    return False
                if is_open(s[index - 1]) and get_related(c) != s[index - 1]:
                    return False
                if is_open(s[index - 1]) and get_related(c) == s[index - 1]:
                    s = s[:index - 1] + s[index + 1:]
                    length -= 2
                    index -= 2
            index += 1
        return len(s) == 0

validation_map = {
    '(': {
        'open': True,
        'related': ')'
    },
    '[': {
        'open': True,
        'related': ']'
    },
    '{': {
        'open': True,
        'related': '}'
    },
    ')': {
        'open': False,
        'related': '('
    },
    ']': {
        'open': False,
        'related': '['
    },
    '}': {
        'open': False,
        'related': '{'
    }
}


def is_open(c):
    return validation_map[c]['open']


def get_related(c):
    return validation_map[c]['related']


Solution().isValid('()')
