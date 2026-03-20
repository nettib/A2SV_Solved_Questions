# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode()

        dummy.next = head

        first = dummy
        prev = head
        node = head.next

        while prev and node:
            temp = node.next
            node.next = prev
            prev.next = temp
            first.next = node
            first = prev
            prev = prev.next
            if prev:
                node = prev.next
        
        return dummy.next

