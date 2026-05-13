# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        _list = []

        for head in lists:
            while head:
                _list.append(head.val)
                head = head.next
        

        heapq.heapify(_list)

        dummy = ListNode()

        if len(_list) > 0:
            head = ListNode(heapq.heappop(_list))
            dummy.next = head
        
        while len(_list) > 0:
            head.next = ListNode(heapq.heappop(_list))
            head = head.next
        
        return dummy.next







# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna