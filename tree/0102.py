class Solution:
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        rsts = []
        stack = [root]
        while stack:
            rst = []
            subtrees = []
            for s in stack:
                if s:
                    rst.append(s.val)
                    subtrees.append(s.left)
                    subtrees.append(s.right)
            if rst:
                rsts.append(rst)
            stack = subtrees
        return rsts