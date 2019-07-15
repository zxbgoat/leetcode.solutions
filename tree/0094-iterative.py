class Solution:

    def inorderTraversal(self, root):
        res, stack = [], []
        p = root
        while p or stack:
            while p:
                stack.append(p.left)
                p = p.left
            top = stack.pop()
            res.append(top.val)
            p = top.right
        return res
