# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        # Reversing the linkedlist
        def reverse_linked_list(head):
            curr = head
            prev = None
            _next = head.next

            while curr:
                curr.next = prev
                prev = curr
                curr = _next
                if curr:
                    _next = curr.next
            
            return prev

        head = reverse_linked_list(head)
        curr = head
        _next = curr.next

        while _next:
            if curr.val <= _next.val:
                curr.next = _next
                curr = _next
                _next = curr.next
            else:
                _next = _next.next
        
        curr.next = None
    
        return reverse_linked_list(head)


        
        



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna