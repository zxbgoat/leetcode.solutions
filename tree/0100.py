class Solution:
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        """
        
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        
        pstack, qstack = [p], [q]
        while pstack and qstack:
            p, q = pstack.pop(), qstack.pop()
            if not check(p, q):
                return False
            if p:
                pstack.append(p.left)
                pstack.append(p.right)
            if q:
                qstack.append(q.left)
                qstack.append(q.right)
        return True