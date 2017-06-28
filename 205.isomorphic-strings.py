#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings
#
# Easy (33.50%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"egg"\n"add"'
#
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map = dict()
        t_map = dict()
        for index, c in enumerate(s):
            char_s = s[index]
            char_t = t[index]
            if char_s not in s_map:
                s_map[char_s] = char_t
            else:
                if char_t != s_map[char_s]:
                    return False
            if char_t not in t_map:
                t_map[char_t] = char_s
            else:
                if char_s != t_map[char_t]:
                    return False
        return True
