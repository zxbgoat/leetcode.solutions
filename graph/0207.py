# Time Limit Exceeded
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjmat[i][j]表示课程i是否依赖于课程j，这样adjmat[i]就表示课程i依赖的所有课程
        adjmat = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        for req in prerequisites:
            adjmat[req[0]][req[1]] = 1
        queue = []
        while len(queue) < numCourses:
            i = 0
            while i < numCourses:
                if not i in queue and not sum(adjmat[i]):
                    break
                i += 1
            if i >= numCourses:
                return False
            queue.append(i)
            for j in range(numCourses):
                adjmat[j][i] = 0
        return True


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegs = [0 for _ in range(numCourses)] # 每个节点的入度
        adjlist = [[] for _ in range(numCourses)] # 每个节点的后继
        queue = []
        for cur, pre in prerequisites:
            indegs[cur] += 1
            adjlist[pre].append(cur)
        for i in range(numCourses):
            if not indegs[i]:
                queue.append(i)
        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adjlist[pre]:
                indegs[cur] -= 1
                if not indegs[cur]:
                    queue.append(cur)
        return not numCourses
