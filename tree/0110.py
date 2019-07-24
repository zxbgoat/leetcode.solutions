class Solution:
    
    def isBalanced(self, root: TreeNode) -> bool:        
        self.flag = True
        
        def getdep(self, root):
            if not root:
                return 0
            ldep = 1 + getdep(self, root.left)
            rdep = 1 + getdep(self, root.right)
            if (ldep - rdep > 1) or (rdep - ldep) > 1:
                self.flag = False
            print(root.val, ldep, rdep)
            return max(ldep, rdep)
        
        getdep(self, root)
        return self.flag


class Solution:
    
    def isBalanced(self, root: TreeNode) -> bool:        
        self.flag = True
        
        def getdep(root):
            if not root:
                return 0
            ldep = 1 + getdep(root.left)
            rdep = 1 + getdep(root.right)
            if (ldep - rdep > 1) or (rdep - ldep) > 1:
                self.flag = False
            print(root.val, ldep, rdep)
            return max(ldep, rdep)
        
        getdep(root)
        return self.flag


# use nonlocal op
class Solution:
    
    def isBalanced(self, root: TreeNode) -> bool:        
        flag = True
        
        def getdep(root):
            if not root:
                return 0
            ldep = 1 + getdep(root.left)
            rdep = 1 + getdep(root.right)
            if (ldep - rdep > 1) or (rdep - ldep) > 1:
                nonlocal flag
                flag = False
            print(root.val, ldep, rdep)
            return max(ldep, rdep)
        
        getdep(root)
        return flag