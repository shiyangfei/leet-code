#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists
#
# Easy (38.96%)
# Total Accepted:    
# Total Submissions: 
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
        head = l1 if l1.val < l2.val else l2
        curr = head
        other = l2 if l1.val < l2.val else l1
        while curr is not None:
            if curr.next is None:
                curr.next = other
                return head
            if other is None:
                return head
            if curr.next.val > other.val:
                holder = curr.next
                curr.next = other
                other = holder
            curr = curr.next
        return head
