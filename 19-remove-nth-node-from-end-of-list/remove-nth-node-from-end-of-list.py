# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            ans2 = None
            return ans2

        temp=head

        idx=1
        while temp.next:
            temp = temp.next
            idx+=1
        
        temp2=head
        ans=temp2
        if idx==n:
            return ans.next
        for i in range(0, idx-n-1):
            temp2=temp2.next

        temp2.next = temp2.next.next

        return ans

        