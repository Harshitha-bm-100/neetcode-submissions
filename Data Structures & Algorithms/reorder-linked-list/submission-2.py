# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find mid
        left = head
        right = head
        while right and right.next:
            left = left.next
            right = right.next.next
        
        curr = left.next
        left.next = None
        #revese second half
        
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node
        
        #combine
        left = head
        right = prev
        while right:
            next_l_node = left.next
            next_r_node = right.next
            left.next = right
            right.next = next_l_node

            left = next_l_node
            right = next_r_node


            
