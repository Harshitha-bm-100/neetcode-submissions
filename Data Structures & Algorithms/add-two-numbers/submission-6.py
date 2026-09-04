# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0
        head = ListNode()
        curr = head

        while curr1 or curr2:
            if not curr1:
                n1 = 0
                n2 = curr2.val
            elif not curr2:
                n1 = curr1.val
                n2 = 0
            else:
                n1 = curr1.val
                n2 = curr2.val
            node = (n1+n2+carry)%10
            carry = (n1+n2+carry)//10

            curr.next = ListNode(node)
            curr = curr.next
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next

        if carry > 0:
            curr.next = ListNode(carry)

        return head.next