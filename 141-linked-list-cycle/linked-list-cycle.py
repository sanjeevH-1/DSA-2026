# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hmap=defaultdict(int)
        curr=head
        while curr:
            if curr not in hmap:
                hmap[curr]
            else:
                return True
            curr=curr.next
        return False

        