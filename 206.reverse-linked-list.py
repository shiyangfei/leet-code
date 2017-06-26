#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list
#
# Easy (45.03%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Can you solve this problem? 🤔
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        node_list = []
        curr = head
        while curr is not None:
            node_list.append(curr)
            curr = curr.next
        length = len(node_list)
        index = length - 1
        while index >= 1:
            node_list[index].next = node_list[index - 1]
            index -= 1
        return node_list[length - 1]
