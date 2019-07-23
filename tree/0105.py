class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # recursive
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:1+idx], inorder[:idx])
        root.right = self.buildTree(preorder[1+idx:], inorder[1+idx:])
        return root