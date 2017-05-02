#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say
#
# Easy (33.64%)
# Total Accepted:    129385
# Total Submissions: 384570
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# 
# 
# Given an integer n, generate the nth sequence.
# 
# 
# 
# Note: The sequence of integers will be represented as a string.
# 
# 
#
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''
        index = 0
        sequence = '1'
        result = sequence
        while index < n - 1:
            current_num = ''
            count = 0
            result = ''
            length = len(sequence)
            for i, num in enumerate(sequence):
                if i == 0:
                    current_num = num
                    count = 1
                if i + 1 >= length:
                    result += str(count) + current_num
                    break
                if i + 1 < length and num != sequence[i + 1]:
                    result += str(count) + current_num
                    count = 0
                    current_num = sequence[i + 1]
                count += 1
            sequence = result
            index += 1
        return result
