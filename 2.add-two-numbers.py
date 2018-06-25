#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (28.86%)
# Total Accepted:    517.9K
# Total Submissions: 1.8M
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
# Example
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
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
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        first_value = (l1.val + l2.val) % 10
        carry = 1 if (l1.val + l2.val) >= 10 else 0
        result = ListNode(first_value)
        cur = result
        l1 = l1.next
        l2 = l2.next
        while (l1 or l2 or carry):
            if l1 is None and carry == 0:
                cur.next = l2
                break
            if l2 is None and carry == 0:
                cur.next = l1
                break
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
            sum = l1.val + l2.val + carry
            value = sum % 10
            carry = 1 if sum >= 10 else 0
            cur.next = ListNode(value)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        return result
