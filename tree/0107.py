class Solution:
    
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        stack, rsts = [root], []
        while stack:
            rst, subtrees = [], []
            for sta in stack:
                if sta:
                    rst.append(sta.val)
                    subtrees.append(sta.left)
                    subtrees.append(sta.right)
            if rst:
                rsts.insert(0, rst)
            stack = subtrees
        return rsts

        # recursive
        """
        rsts, roots = [], [root]
        
        def level(roots):
            if not roots:
                return None
            rst, subtrees = [], []
            for root in roots:
                if root:
                    rst.append(root.val)
                    subtrees.append(root.left)
                    subtrees.append(root.right)
            if rst:
                rsts.insert(0, rst)
            level(subtrees)
        
        level(roots)
        return rsts
        """