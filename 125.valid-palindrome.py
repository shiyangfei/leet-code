#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome
#
# Easy (25.94%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""'
#
# 
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# 
# 
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# 
# 
# 
# Note:
# Have you consider that the string might be empty? This is a good question to
# ask during an interview.
# 
# For the purpose of this problem, we define empty string as valid palindrome.
# 
#
def transfer_case(code):
    if 97 <= code <= 122 or 48 <= code <= 57:
        return code
    if 65 <= code <= 90:
        return code + 32
    return None


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = True
        length = len(s)
        if length == 0:
            return result
        left = 0
        right = length - 1
        while left < right:
            left_c = s[left]
            right_c = s[right]
            left_code = transfer_case(ord(left_c))
            right_code = transfer_case(ord(right_c))
            if left_code is None:
                left += 1
                continue
            if right_code is None:
                right -= 1
                continue
            if left_code != right_code:
                result = False
                break
            left += 1
            right -= 1
        return result
