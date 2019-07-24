class Solution:
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        self.flag = False
        if not root:
            return self.flag
        
        def sumpath(node, pval):
            if not node.left and not node.right:
                if node.val + pval == sum:
                    self.flag = True
                return
            if node.left:
                sumpath(node.left, node.val + pval)
            if node.right:
                sumpath(node.right, node.val + pval)
        
        sumpath(root, 0)
        return self.flag
        """

        if not root:
            return False
        print(sum, root.val)
        if not root.left and not root.right:
            return root.val == sum
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)