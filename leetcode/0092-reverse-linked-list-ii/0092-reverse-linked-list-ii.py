# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        special = None
        dummy = ListNode()
        dummy.next = head

        count = 1
        flag = 0
        prev = dummy
        curr = head
        nex = head.next

        while curr:
            if count == left:
                special = prev
            if count > left and count <= right:
                curr.next = prev
            if count > right:
                flag = 1
                special.next.next = curr
                special.next = prev
                break
            count += 1
            prev = curr
            curr = nex
            nex = curr.next if curr else None
        
        if flag == 0:
            flag = 1
            special.next.next = curr
            special.next = prev
        
        return dummy.next


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna