class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preq = defaultdict(list)
        for crs, pq in prerequisites:
            preq[crs].append(pq)
        
        taken = set()

        def dfs(crs):
            # cycle detected
            if crs in taken:
                return False
            # if no preq can also write as if not preq[crs]    
            if preq[crs] == []:
                return True
            
            taken.add(crs)
            for pre in preq[crs]:
                if not dfs(pre):
                    return False
            taken.remove(crs)
            preq[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        