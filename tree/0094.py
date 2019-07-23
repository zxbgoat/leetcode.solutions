# recursive
class Solution:
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


class Solution:
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return res


# iterative
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
