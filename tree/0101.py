class Solution:
    
    def isSymmetric(self, root: TreeNode) -> bool:

        # recursive
        """
        def isMirror(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val \
                   and isMirror(p.left, q.right) \
                   and isMirror(p.right, q.left)

        return isMirror(root, root)
        """
        
        # iterative
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        
        stack1 = [root]
        stack2 = [root]
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if not check(node1, node2):
                return False
            if node1:
                stack1.append(node1.left)
                stack1.append(node1.right)
            if node2:
                stack2.append(node2.right)
                stack2.append(node2.left)
        return True