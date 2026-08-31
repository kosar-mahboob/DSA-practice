# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prev = head
        curr = head.next
        nxt = curr.next
        pos = 1          # index of curr (0-based, head is 0)
        first = -1
        last = -1
        min_dist = float('inf')

        while nxt:
            # local maxima or minima
            if (curr.val > prev.val and curr.val > nxt.val) or \
               (curr.val < prev.val and curr.val < nxt.val):
                if first == -1:
                    first = pos
                else:
                    min_dist = min(min_dist, pos - last)
                last = pos

            prev = curr
            curr = nxt
            nxt = nxt.next
            pos += 1

        if first == last:
            return [-1, -1]

        return [min_dist, last - first]