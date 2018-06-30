#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (25.51%)
# Total Accepted:    333.4K
# Total Submissions: 1.3M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution(object):
    def get_odd_palin(self, s, i):
        result = ''
        start = i
        end = i
        while True:
            if start < 0 or end >= len(s):
                return result
            if s[start] != s[end]:
                return result
            result = s[start: end + 1]
            start -= 1
            end += 1

    def get_even_palin(self, s, i):
        result = ''
        start = i - 1
        end = i
        while True:
            if start < 0 or end >= len(s):
                return result
            if s[start] != s[end]:
                return result
            result = s[start: end + 1]
            start -= 1
            end += 1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or s == '':
            return None
        i = 0
        result = ''
        while True:
            if i >= len(s):
                break
            odd_palin = self.get_odd_palin(s, i)
            even_palin = self.get_even_palin(s, i)
            palin = odd_palin if len(odd_palin) > len(even_palin) else even_palin
            result = result if len(result) > len(palin) else palin
            i += 1
        return result
