# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Find middle (slow & fast pointers)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half starting from slow
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # Step 3: Sum pairs: first half (head) and reversed second half (prev)
        max_sum = 0
        first, second = head, prev
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next
        
        return max_sum
