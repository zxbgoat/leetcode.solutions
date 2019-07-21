# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        # recursive
        """
        def valid(node, lower, higher):
            if not node:
                return True
            val  = node.val
            if val <= lower or val >= higher:
                return False
            if not valid(node.left, lower, val):
                return False
            if not valid(node.right, val, higher):
                return False
            return True
        return valid(root, float('-inf'), float('inf'))
        """
        # iteration
        """
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, higher = stack.pop()
            if not node:
                continue
            if node.val >= higher or node.val <= lower:
                return False
            stack.append((node.left, lower, node.val))
            stack.append((node.right, node.val, higher))
        return True
        """
        # inorder
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True