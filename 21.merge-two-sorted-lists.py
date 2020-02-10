#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (51.09%)
# Total Accepted:    833.2K
# Total Submissions: 1.6M
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
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        curr_l1 = l1
        curr_l2 = l2
        start = ListNode(None)
        curr = start
        while curr_l1 or curr_l2:
            if curr_l2 is None:
                curr.next = curr_l1
                curr_l1 = curr_l1.next
            elif curr_l1 is None:
                curr.next = curr_l2
                curr_l2 = curr_l2.next
            elif curr_l1.val < curr_l2.val:
                curr.next = curr_l1
                curr_l1 = curr_l1.next
            else:
                curr.next = curr_l2
                curr_l2 = curr_l2.next
            curr = curr.next
        return start.next
