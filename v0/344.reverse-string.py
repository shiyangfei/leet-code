#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string
#
# Easy (58.85%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and returns the string
# reversed.
# 
# 
# Example:
# Given s = "hello", return "olleh".
# 
#
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length <= 1:
            return s
        s = list(s)
        start = 0
        end = length - 1
        while start < end:
            holder = s[start]
            s[start] = s[end]
            s[end] = holder
            start += 1
            end -= 1
        return "".join(s)

