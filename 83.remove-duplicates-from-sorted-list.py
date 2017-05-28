#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list
#
# Easy (39.48%)
# Total Accepted:    177237
# Total Submissions: 448937
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
        if node is not None and node.next is not None:
            if node.val == node.next.val:
                return self.helper(node.next)
            else:
                return node.next

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur is not None and cur.next is not None:
            if cur.next.val == cur.val:
                next_node = self.helper(cur.next)
            else:
                next_node = cur.next
            cur.next = next_node
            cur = cur.next
        return head
