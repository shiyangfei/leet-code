#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string
#
# Easy (38.31%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# 
# Example 1:
# Given s = "hello", return "holle".
# 
# 
# 
# Example 2:
# Given s = "leetcode", return "leotcede".
# 
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
#
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # TODO: be aware of upper case char
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        length = len(s)
        if length <= 1:
            return s
        s = list(s)
        start = 0
        end = length - 1
        while start < end:
            if s[start] not in vowels:
                start += 1
                continue
            if s[end] not in vowels:
                end -= 1
                continue
            holder = s[start]
            s[start] = s[end]
            s[end] = holder
            start += 1
            end -= 1
        return "".join(s)
