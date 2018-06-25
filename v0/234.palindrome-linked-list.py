#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list
#
# Easy (32.45%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reverse, fast = None, head
        # Reverse the first half part of the list.
        while fast and fast.next:
            fast = fast.next.next
            next_node = head.next
            head.next = reverse
            reverse = head
            head = next_node

        # If the number of the nodes is odd,
        # set the head of the tail list to the next of the median node.
        tail = head.next if fast else head

        # Compare the reversed first half list with the second half list.
        # And restore the reversed first half list.
        while reverse:
            if reverse.val == tail.val:
                next_node = reverse.next
                reverse.next = head
                head = reverse
                reverse = next_node
                tail = tail.next
            else:
                return False
        return True
