#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle
#
# Easy (35.45%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\nno cycle'
#
# 
# Given a linked list, determine if it has a cycle in it.
# 
# 
# 
# Follow up:
# Can you solve it without using extra space?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        p1 = p2 = head
        while True:
            if p2.next:
                p1 = p1.next
                p2 = p2.next.next
                if p1 is None or p2 is None:
                    return False
                if p1 is p2:
                    return True
            else:
                return False
