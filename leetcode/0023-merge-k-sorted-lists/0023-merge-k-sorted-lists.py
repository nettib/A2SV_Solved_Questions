# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for _list in lists:
            node = _list
            while node:
                heappush(heap, node.val)
                node = node.next
        
        dummy = ListNode()
        if len(heap) > 0:
            head = ListNode(heappop(heap))
            dummy.next = head

        while len(heap) > 0:
            head.next = ListNode(heappop(heap))
            head = head.next
        
        return dummy.next
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna