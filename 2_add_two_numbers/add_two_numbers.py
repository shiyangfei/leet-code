class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.val == 0 and l1.next is None:
            return l2
        if l2.val == 0 and l1.next is None:
            return l1
        result = None
        current = None
        carry = 0
        while l1 is not None or l2 is not None:
            val_1 = l1.val if (l1 is not None) else 0
            val_2 = l2.val if (l2 is not None) else 0
            val_sum = val_1 + val_2 + carry
            carry = 1 if val_sum >= 10 else 0
            val = val_sum if val_sum >= 10 else val_sum - 10
            node = ListNode(val)
            if result is None:
                result = node
            if current is not None:
                current.next = node
            current = node
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if carry > 0:
            current.next = ListNode(carry)
        return result
