#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix
#
# Easy (31.41%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        result = ''
        index = 0
        while True:
            c = ''
            for string in strs:
                if len(string) - 1 < index:
                    return result
                if c == '':
                    c = string[index]
                else:
                    if string[index] != c:
                        return result
            result += c
            index += 1
