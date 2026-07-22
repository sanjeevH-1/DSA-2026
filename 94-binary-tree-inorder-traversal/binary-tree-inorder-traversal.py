# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        # Traverse as long as there are unvisited nodes (cur) or stacked ancestors
        while cur or stack:
            # 1. Reach the leftmost node of the current subtree
            while cur:
                stack.append(cur)  # Save root/parent node before moving left
                cur = cur.left

            # 2. Backtrack from the bottom left
            cur = stack.pop()
            res.append(cur.val)    # Process Left / Root node

            # 3. Move to the right subtree
            cur = cur.right

        return res