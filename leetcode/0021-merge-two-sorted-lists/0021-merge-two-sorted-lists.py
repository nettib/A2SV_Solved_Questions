# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        head = ListNode()
        head1 = list1
        head2 = list2

        curr = head 

        while head1 and head2:
            if head1.val < head2.val:
                curr.next = head1
                curr = head1
                head1 = curr.next
                curr.next = None
            else:
                curr.next = head2
                curr = head2
                head2 = curr.next
                curr.next = None
        
        if head1:
            curr.next = head1
        
        if head2:
            curr.next = head2
        
        return head.next


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna