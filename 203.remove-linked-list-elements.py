#
# @lc app=leetcode id=203 lang=python
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (37.04%)
# Total Accepted:    285.5K
# Total Submissions: 769.1K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example:
# 
# 
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        last = None
        curr = head
        while curr is not None:
            if curr.val == val:
                # remove node
                if last is None:
                    head = curr.next
                else:
                    last.next = curr.next
                curr = curr.next
            else:
                last = curr
                curr = curr.next
        return head
