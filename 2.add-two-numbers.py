#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.69%)
# Total Accepted:    1.4M
# Total Submissions: 4.1M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        res = ListNode()
        res_cur = res
        carry = 0
        cur_1 = l1
        cur_2 = l2
        while cur_1 is not None or cur_2 is not None:
            v1 = cur_1.val if cur_1 is not None else 0
            v2 = cur_2.val if cur_2 is not None else 0
            v = (v1 + v2 + carry) % 10
            res_cur.next = ListNode()
            res_cur.next.val = v
            res_cur = res_cur.next
            carry = 1 if (v1 + v2 + carry) >= 10 else 0
            cur_1 = cur_1.next if cur_1 is not None else None
            cur_2 = cur_2.next if cur_2 is not None else None
        if carry > 0:
            res_cur.next = ListNode()
            res_cur.next.val = carry
        return res.next

