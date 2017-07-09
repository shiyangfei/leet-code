#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list
#
# Easy (39.47%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# 
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
# 
# 
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def helper(self, node):
        if node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
                return self.helper(node)
            else:
                return node
        else:
            return node

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr is not None:
            curr = self.helper(curr)
            curr = curr.next
        return head
