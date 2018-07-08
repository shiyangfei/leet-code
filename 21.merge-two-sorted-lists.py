#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (42.10%)
# Total Accepted:    370.2K
# Total Submissions: 878.5K
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
    def helper(self, n1, n2, cur):
        if n1 is None and n2 is None:
            return
        if n1 is None:
            cur.next = n2
            n2 = n2.next
        elif n2 is None:
            cur.next = n1
            n1 = n1.next
        else:
            if n1.val <= n2.val:
                cur.next = n1
                n1 = n1.next
            else:
                cur.next = n2
                n2 = n2.next
        cur = cur.next
        self.helper(n1, n2, cur)

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
        dummy = ListNode(-1)
        self.helper(l1, l2, dummy)
        return dummy.next
