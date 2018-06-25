#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note
#
# Easy (46.95%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"a"\n"b"'
#
# 
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom 
# note can be constructed from the magazines ; otherwise, it will return
# false. 
# 
# 
# Each letter in the magazine string can only be used once in your ransom
# note.
# 
# 
# Note:
# You may assume that both strings contain only lowercase letters.
# 
# 
# 
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
# 
# 
#
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_map = dict()
        for index1, char1 in enumerate(magazine):
            if char1 not in char_map:
                char_map[char1] = 0
            char_map[char1] += 1
        for index2, char2 in enumerate(ransomNote):
            if char2 not in char_map or char_map[char2] == 0:
                return False
            else:
                char_map[char2] -= 1
        return True
