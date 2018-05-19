#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (41.19%)
# Total Accepted:    338K
# Total Submissions: 820.4K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
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
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            result_root = l1
            node1 = l1.next
            node2 = l2
        else:
            result_root = l2
            node1 = l1
            node2 = l2.next
        result_curr = result_root
        while True:
            if node1 is None and node2 is None:
                return result_root
            if node1 is not None and node2 is None:
                result_curr.next = node1
                return result_root
            if node1 is None and node2 is not None:
                result_curr.next = node2
                return result_root
            if node1 is not None and node2 is not None:
                if node1.val <= node2.val:
                    result_curr.next = node1
                    node1 = node1.next
                else:
                    result_curr.next = node2
                    node2 = node2.next
                result_curr = result_curr.next
