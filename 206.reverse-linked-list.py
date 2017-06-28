#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list
#
# Easy (45.03%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self.reverse(n, node)

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(head)
