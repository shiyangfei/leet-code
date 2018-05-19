#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (48.46%)
# Total Accepted:    213.1K
# Total Submissions: 439.8K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
class Solution(object):
    def helper(self, input_string, left_inv, right_inv, open_left_count, result):
        if left_inv == 0 and right_inv == 0:
            result.append(input_string)
            return
        if left_inv == 0:
            result.append((input_string + ')' * right_inv))
            return
        self.helper(input_string + '(', left_inv - 1, right_inv, open_left_count + 1, result)
        if open_left_count > 0:
            self.helper(input_string + ')', left_inv, right_inv - 1, open_left_count - 1, result)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = list()
        left_inv = n
        right_inv = n
        open_left_count = 0
        self.helper('', left_inv, right_inv, open_left_count, result)
        return result
