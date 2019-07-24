class Solution:
    
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        self.paths = []
        if not root:
            return self.paths
        
        def sumpath(root, path):
            print(root.val, path)
            if not root.left and not root.right:
                if sum(path + [root.val]) == s:
                    self.paths.append(path+[root.val])
                return
            if root.left:
                sumpath(root.left, path+[root.val])
            if root.right:
                sumpath(root.right, path+[root.val])
        
        sumpath(root, [])
        return self.paths