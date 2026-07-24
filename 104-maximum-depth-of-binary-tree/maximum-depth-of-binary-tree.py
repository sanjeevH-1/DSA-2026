# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BASE CASE: An empty tree (or reaching beyond a leaf node) has a depth of 0.
        if not root:
            return 0
        
        # RECURSIVE STEP:
        # 1. Compute the maximum depth of the left subtree.
        left_depth = self.maxDepth(root.left)
        
        # 2. Compute the maximum depth of the right subtree.
        right_depth = self.maxDepth(root.right)
        
        # 3. The total depth at the current node is 1 (for the current node itself)
        #    plus the maximum depth between its left and right subtrees.
        return 1 + max(left_depth, right_depth)