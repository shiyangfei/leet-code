#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements
#
# Easy (32.02%)
# Total Accepted:    113563
# Total Submissions: 354669
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6,  val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
# 
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
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
        if head is None:
            return head
        while head is not None and head.val == val:
            head = head.next
        curr = head
        while curr is not None and curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
