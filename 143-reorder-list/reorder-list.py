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
        # STEP 1: Find the middle of the linked list
        # We use slow/fast pointers. By the time fast reaches the end,
        # slow will be at the midpoint.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # STEP 2: Reverse the second half of the list
        # 'second' is the start of the second half.
        second = slow.next
        # Break the link between the two halves to form two separate lists.
        slow.next = None
        
        prev, curr = None, second
        while curr:
            nxt = curr.next
            curr.next = prev  # Reversing the pointer
            prev = curr       # Move prev forward
            curr = nxt        # Move curr forward
        
        # STEP 3: Merge the two lists by interleaving nodes
        # 'prev' is now the head of the reversed second half.
        first, second = head, prev
        while first and second:  
            # Temporarily store next nodes to avoid losing the rest of the lists
            tmp1, tmp2 = first.next, second.next
            
            # Re-stitch: first -> second -> original_first_next
            first.next = second
            second.next = tmp1
            
            # Advance pointers for the next iteration
            first, second = tmp1, tmp2