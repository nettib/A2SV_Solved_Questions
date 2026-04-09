# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(node1, node2):
            dummy = ListNode()
            curr = dummy 
            while node1 and node2:
                if node1.val <= node2.val:
                    curr.next = node1
                    curr = node1
                    node1 = node1.next
                else:
                    curr.next = node2
                    curr = node2
                    node2 = node2.next
                
            while node1:
                curr.next = node1
                curr = node1
                node1 = node1.next
            while node2:
                curr.next = node2
                curr = node2
                node2 = node2.next
            
            return dummy.next
        
        def get_mid(node):
            s, f = node, node.next
            while f and f.next:
                s = s.next
                f = f.next.next
            
            return s

        def merge_sort(head):
            if not head or not head.next:
                return head
            
            left = head
            right = get_mid(head)
            tmp = right.next
            right.next = None
            right = tmp 

            left_part = merge_sort(left)
            right_part = merge_sort(right)

            return merge(left_part, right_part)
        
        return merge_sort(head)


            