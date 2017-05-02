#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers
#
# Medium (27.22%)
# Total Accepted:    280108
# Total Submissions: 1029214
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = None
        current = None
        carry = 0
        while l1 is not None or l2 is not None:
            val_1 = l1.val if (l1 is not None) else 0
            val_2 = l2.val if (l2 is not None) else 0
            val_sum = val_1 + val_2 + carry
            carry = 1 if val_sum >= 10 else 0
            val = val_sum if val_sum < 10 else val_sum - 10
            node = ListNode(val)
            if result is None:
                result = node
            if current is not None:
                current.next = node
            current = node
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if carry > 0:
            current.next = ListNode(carry)
        return result
