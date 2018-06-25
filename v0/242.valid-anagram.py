#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram
#
# Easy (46.09%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""\n""'
#
# Given two strings s and t, write a function to determine if t is an anagram
# of s. 
# 
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
#
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c_map = dict()
        for index, c in enumerate(s):
            if c in c_map:
                c_map[c] += 1
            else:
                c_map[c] = 1
        for index, c in enumerate(t):
            if c not in c_map or c_map[c] == 0:
                return False
            else:
                c_map[c] -= 1
            if c_map[c] == 0:
                del c_map[c]
        return len(c_map.keys()) == 0
