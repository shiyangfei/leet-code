#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string
#
# Easy (46.38%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return -1
        if length == 1:
            return 0
        char_map = dict()
        for index, c in enumerate(s):
            if c not in char_map:
                char_map[c] = index
            else:
                char_map[c] = -1
        result = None
        for key in char_map:
            if char_map[key] != -1:
                if result is None:
                    result = char_map[key]
                elif char_map[key] < result:
                    result = char_map[key]
        return result if result is not None else -1
