"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        # 1. Map None to None to safely handle terminal pointers (.next / .random pointing to None)
        hmap = {None: None}
        
        # 2. First Pass: Clone every node and map the original node to its copy
        cur = head
        while cur:
            newNode = Node(cur.val)
            hmap[cur] = newNode  # Key: Original Node -> Value: Isolated Copy Node
            cur = cur.next

        # 3. Second Pass: Wire up the next and random pointers of the copy nodes
        curr = head
        while curr:
            copy = hmap[curr]  # Retrieve the corresponding copied node
            
            # Use hmap to find where the copied next/random nodes should point.
            # e.g., if curr.next is Node B, then copy.next should point to hmap[Node B] (which is B')
            copy.next = hmap[curr.next]
            copy.random = hmap[curr.random]
            
            curr = curr.next

        # 4. Return the cloned head node (if head is None, hmap[None] safely returns None)
        return hmap[head]