# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Helper function to recursively invert the tree starting from a given node
        def help(root):
            # Base case: if the current node is None, stop recursion
            if not root:
                return None
            
            # Swap the left and right child nodes
            root.left, root.right = root.right, root.left

            # Recursively call help on the newly swapped left child
            help(root.left)
            # Recursively call help on the newly swapped right child
            help(root.right)

        # Kick off the recursive process starting at the tree's root
        help(root)
        
        # Return the original root node after all nodes have been inverted
        return root