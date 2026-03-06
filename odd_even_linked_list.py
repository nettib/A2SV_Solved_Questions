# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        curr = head
        curr_next = head.next
        mark = head.next

        while curr_next and curr_next.next:
            curr.next = curr.next.next
            curr = curr.next
            curr_next.next = curr_next.next.next
            curr_next = curr_next.next
        
        curr.next = mark

        return head
            
