#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (28.64%)
# Total Accepted:    480.4K
# Total Submissions: 1.7M
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
    def helper(self, node1, node2, carry):
        v1 = 0 if node1 is None else node1.val
        v2 = 0 if node2 is None else node2.val
        temp = v1 + v2 + carry
        if temp >= 10:
            temp = temp - 10
            carry = 1
        else:
            carry = 0
        node = ListNode(temp)
        n1 = node1.next if node1 is not None else None
        n2 = node2.next if node2 is not None else None
        if not (n1 is None and n2 is None and carry == 0):
            node.next = self.helper(n1, n2, carry)
        return node

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None

        carry = 0
        return self.helper(l1, l2, carry)
