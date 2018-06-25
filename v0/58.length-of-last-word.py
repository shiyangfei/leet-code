#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word
#
# Easy (31.54%)
# Total Accepted:    139260
# Total Submissions: 441426
# Testcase Example:  '""'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space
# characters only.
# 
# 
# For example, 
# Given s = "Hello World",
# return 5.
# 
#
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        array = s.split(' ')
        length = len(array)
        index = length - 1
        while index >= 0:
            item = array[index]
            # only if the item is a valid word, return its len
            if len(item) > 0:
                return len(item)
            else:
                index -= 1
        # cannot find a valid word. return 0
        return 0
