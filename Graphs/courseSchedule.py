'''
Course Schedule : if all courses are possible 
using DFS approach 
we use a adjacency list(Hash Map) for finding out courses which does not has any pre req.
empty list states it can be completed 
complexity ; O(n + p)  Nodes + pre requisite
have a visited set to keep check of loop 
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        # map each course to : pre req list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # keep track of already visited courses
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        # nested approach to accomodate for disconnected graph 
        for c in range(numCourses):
            if not dfs(c):
                return False
            return True       