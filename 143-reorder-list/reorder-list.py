# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # find the mid ele

        slow, fast = head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        # reverse the secinnd half
        second = slow.next
        slow.next = None # brk the first link
        prev, curr= None, second
        while curr:
            nxt=curr.next
            curr.next=prev
            prev = curr
            curr = nxt

        
        # merge 2 list
        first, second = head, prev
        
        while first and second:
            tmp1,tmp2 = first.next, second.next
            first.next = second
            second.next= tmp1
            first, second = tmp1, tmp2



        