class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preq_map = {crs:[] for crs in range(numCourses)}
        for crs, pq in prerequisites:
            preq_map[crs].append(pq)
        
        visit , cycle = set(), set()
        result = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in preq_map[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            result.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return result
        