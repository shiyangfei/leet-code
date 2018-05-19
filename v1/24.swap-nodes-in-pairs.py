#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (39.45%)
# Total Accepted:    216.5K
# Total Submissions: 548.8K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# Note:
# 
# 
# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def helper(self, last_node, node):
        if node is None:
            return
        node_a = node
        node_b = node.next
        if node_b is None:
            return node_a
        node_b_next = node_b.next
        if last_node:
            last_node.next = node_b
        node_b.next = node_a
        node_a.next = node_b_next
        self.helper(node_a, node_a.next)
        return node_b

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.helper(None, head)
