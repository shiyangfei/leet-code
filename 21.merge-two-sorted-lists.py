#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists
#
# Easy (38.61%)
# Total Accepted:    213008
# Total Submissions: 551673
# Testcase Example:  '[]\n[]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        result = l1 if l1.val < l2.val else l2
        current_node = result
        compare_node = l2 if l1.val < l2.val else l1
        while current_node is not None and compare_node is not None:
            if current_node.next is None:
                current_node.next = compare_node
                break
            next_val = current_node.next.val
            compare_val = compare_node.val
            if next_val <= compare_val:
                current_node = current_node.next
            else:
                next_node = current_node.next
                current_node.next = compare_node
                current_node = compare_node
                compare_node = next_node
        return result
