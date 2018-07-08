#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (48.99%)
# Total Accepted:    224.3K
# Total Submissions: 457.5K
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
    def helper(self, cur, num_open_to_use, num_open_open, n):
        if len(cur) == n * 2:
            self.candidates[cur] = True
            return
        if num_open_to_use > 0:
            if num_open_open:
                self.helper(cur + '(', num_open_to_use - 1, num_open_open + 1, n)
                self.helper(cur + ')', num_open_to_use, num_open_open - 1, n)
            else:
                self.helper(cur + '(', num_open_to_use - 1, num_open_open + 1, n)
        else:
            self.helper(cur + ')', num_open_to_use, num_open_open - 1, n)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.candidates = dict()
        self.helper('', n, 0, n)
        for item in self.candidates:
            res.append(item)
        return res
