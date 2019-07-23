class Solution:
    
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        lev, rsts, stack = 0, [], [root]
        while any(stack):
            subtrees = []
            if lev % 2:
                rst = [stack[i].val for i in range(len(stack)-1, -1, -1) if stack[i]]
            else:
                rst = [stack[i].val for i in range(len(stack)) if stack[i]]
            for sta in stack:
                if sta:
                    subtrees.append(sta.left)
                    subtrees.append(sta.right)
            rsts.append(rst)
            lev += 1
            stack = subtrees
        return rsts