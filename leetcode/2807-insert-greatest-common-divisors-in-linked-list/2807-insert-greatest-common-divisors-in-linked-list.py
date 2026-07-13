# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if b > a:
                a, b = b, a
            while b != 0:
                a, b = b, a % b
            
            return a
        
        curr = head

        # while curr.next:
        #     val = gcd(curr.val, curr.next.val)
        #     temp = curr.next
        #     node = ListNode(val)
        #     curr.next = node
        #     node.next = temp

        while curr.next:
            val = gcd(curr.val, curr.next.val)
            node = ListNode(val)
            node.next = curr.next
            curr.next = node
            curr = node.next
        
        return head



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna