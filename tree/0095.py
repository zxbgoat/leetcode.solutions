class Solution:
        
    def generateTrees(self, n: int) -> List[TreeNode]:

        def gentrees(start, end):
            if start > end:
                return [None,]
            trees = []
            for i in range(start, end+1):
                ltrees = gentrees(start, i-1)
                rtrees = gentrees(i+1, end)
                for l in ltrees:
                    for r in rtrees:
                        ctree = TreeNode(i)
                        ctree.left = l
                        ctree.right = r
                        trees.append(ctree)
            return trees

        return gentrees(1, n) if n else []
