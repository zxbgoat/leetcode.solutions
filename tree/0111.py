class Solution:
    
    def minDepth(self, root: TreeNode) -> int:
        
        def mindep(root):
            if not root:
                return 0
            if root.left and root.right:
                return 1 + min(mindep(root.left), mindep(root.right))
            else:
                return 1 + max(mindep(root.left), mindep(root.right))
        
        return mindep(root)