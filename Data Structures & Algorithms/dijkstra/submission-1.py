class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        # create adjacency list
        adj = {i:[] for i in range(n)}

        for sr, dst, wt in edges:
            adj[sr].append([dst, wt])
        
        # min heap has (cost,node) because we want to always pop the smallest weighted
        # path from a particular node
        min_heap = [[0, src]]
        shortest = {}

        while min_heap:
            wt1 , n1 = heapq.heappop(min_heap)

            if n1 in shortest:
                continue
            shortest[n1] = wt1

            for n2 , wt2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(min_heap,[wt1+wt2, n2])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1            
        return shortest
