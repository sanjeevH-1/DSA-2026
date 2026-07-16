# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Initialize arrays to store values from the linked lists
        res1, res2 = [], []

        # 2. Traverse l1 and l2, extracting node values into Python lists
        while l1 or l2:
            if l1:
                res1.append(l1.val)
                l1 = l1.next
            if l2:
                res2.append(l2.val)
                l2 = l2.next

        # 3. Reverse the arrays because the input linked lists are given in reverse order
        res1.reverse()
        res2.reverse()

        # 4. Reconstruct the actual mathematical integer for the first number
        result = 0
        for digit in res1:
            result = result * 10 + digit
            
        # 5. Reconstruct the actual mathematical integer for the second number
        result1 = 0
        for digit in res2:
            result1 = result1 * 10 + digit
            
        # 6. Add both numbers together
        ans = result + result1

        # Edge Case: If the sum is 0, return a single node containing 0
        if ans == 0:
            return ListNode(0)

        # 7. Extract digits from the sum back into a list (this naturally reverses them)
        n = ans
        new_array = []
        while n:
            digit = n % 10          # Get the last digit (right-most)
            new_array.append(digit) # Append it
            n = n // 10             # Chop off the last digit
 
        # 8. Rebuild a new linked list from the reversed digits
        dummy_head = ListNode()     # Dummy node to anchor the start of the list
        current = dummy_head
        
        for i in new_array:
            current.next = ListNode(i) # Point to the new node
            current = current.next     # Move the pointer forward
            
        current.next = None         # Ensure the tail node's next is explicitly set to None
        
        return dummy_head.next      # Return the head of the reconstructed list (skipping the dummy node)