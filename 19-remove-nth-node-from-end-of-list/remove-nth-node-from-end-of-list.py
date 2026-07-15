# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Base Case: If the list has only one node, removing it leaves an empty list.
        if not head.next:
            return None

        # 2. First Pass: Find the total length (idx) of the linked list.
        temp = head
        idx = 1
        while temp.next:
            temp = temp.next
            idx += 1
        
        # 3. Edge Case: If the target node is the head node (n equals total length).
        # We simply skip the head by returning head.next (ans.next).
        ans = head
        if idx == n:
            return ans.next
            
        # 4. Second Pass: Traverse to the node right BEFORE the one we want to delete.
        # The loop runs exactly (idx - n - 1) times.
        temp2 = head
        for i in range(0, idx - n - 1):
            temp2 = temp2.next

        # 5. Deletion: Bypass the target node by linking to the node after it.
        temp2.next = temp2.next.next

        # 6. Return the original head (or updated head if handled by the edge case).
        return ans