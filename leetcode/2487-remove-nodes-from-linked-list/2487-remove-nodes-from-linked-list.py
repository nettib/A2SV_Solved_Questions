# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        arr = []

        curr = head

        while curr:
            while arr and arr[-1] < curr.val:
                arr.pop()
            arr.append(curr.val)
            curr = curr.next
        
        head = ListNode()
        curr = head
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        
        return head.next

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna