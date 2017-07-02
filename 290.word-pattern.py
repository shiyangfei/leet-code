#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern
#
# Easy (32.83%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# ⁠Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Examples:
# 
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# 
# 
# 
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.
# 
# 
# Credits:Special thanks to @minglotus6 for adding this problem and creating
# all test cases.
#
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        words_length = len(words)
        patten_length = len(pattern)
        if words_length != patten_length:
            return False
        pattern_map = dict()
        word_map = dict()
        for index, word in enumerate(words):
            letter = pattern[index]
            if letter not in pattern_map:
                pattern_map[letter] = word
            else:
                if pattern_map[letter] != word:
                    return False

            if word not in word_map:
                word_map[word] = letter
            else:
                if word_map[word] != letter:
                    return False
        return True
