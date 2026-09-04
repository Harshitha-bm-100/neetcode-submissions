# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        count = 1
        while right.next:
            count+=1
            right = right.next

        left = head
        if count == n:
            return left.next
        
        while count > (n+1):
            left = left.next
            count -= 1
        left.next = left.next.next
        return head