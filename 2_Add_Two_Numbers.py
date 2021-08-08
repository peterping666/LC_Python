from typing import Optional

from ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        carry = 0
        val = 0
        cur = head
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry = val // 10
            val %= 10
            cur.next = ListNode(val)
            cur = cur.next
        if carry:
            cur.next = ListNode(carry)
        return head.next