# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Special case: only one node
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        prev = None
        
        # Fast moves 2 steps, slow moves 1 step
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node (slow)
        prev.next = slow.next
        
        return head
