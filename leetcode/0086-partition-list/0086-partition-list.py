# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy2 = ListNode()

        curr1 = dummy1
        curr2 = dummy2
        curr = head

        while curr:
            if curr.val < x:
                curr1.next = curr
                curr = curr.next
                curr1 = curr1.next
                curr1.next = None
            else:
                curr2.next = curr
                curr = curr.next
                curr2 = curr2.next
                curr2.next = None
        
        curr1.next = dummy2.next
        dummy2.next = None

        return dummy1.next
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna