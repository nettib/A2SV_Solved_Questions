# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        tail = head
        while curr:
            length += 1
            tail = curr
            curr = curr.next
        
        if not head or length == k:
            return head

        sign = None

        if length > k:
            sign = length - k
        else:
            sign = length - (k % length)
        
        count = 1
        curr = head
        while count != sign:
            count += 1
            curr = curr.next
        
        tail.next = head
        head = curr.next
        curr.next = None

        return head

        
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna