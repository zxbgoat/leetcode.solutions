class Solution:
    
    def maxDepth(self, root: TreeNode) -> int:
        # recursive, inorder
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        """
        # iterative, levelorder
        depth, stack = 0, [root]
        while any(stack):
            depth += 1
            subtrees = []
            for node in stack:
                if node:
                    subtrees.append(node.left)
                    subtrees.append(node.right)
            stack = subtrees
        return depth