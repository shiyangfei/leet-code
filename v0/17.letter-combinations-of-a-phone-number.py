#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number
#
# Medium (33.75%)
# Total Accepted:    144926
# Total Submissions: 429375
# Testcase Example:  '""'
#
# Given a digit string, return all possible letter combinations that the number
# could represent.
# 
# 
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below.
# 
# 
# 
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# 
# Note:
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
# 
#
class Solution(object):
    def __init__(self):
        self.map = {
            '0': [''],
            '1': [''],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    def helper(self, digits, index, res, line):
        if len(line) == len(digits):
            res.append(''.join([x for x in line]))
            return
        for l in self.map[digits[index]]:
            line.append(l)
            self.helper(digits, index + 1, res, line)
            line.pop()

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        res = []
        line = []
        self.helper(digits, 0, res, line)
        return res
