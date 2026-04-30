class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        #create adjacency list for nodes
        adj = {i:[] for i in range(1, n+1)}

        for u,v,t in times:
            adj[u].append([v,t])
        
        shortest = {}
        min_heap = [(0, k)]

        while min_heap:
            t1, n1 = heapq.heappop(min_heap)

            if n1 in shortest:
                continue
            shortest[n1] = t1

            for neighbor , t2 in adj[n1]:
                if neighbor not in shortest:
                    heapq.heappush(min_heap, [t1+t2, neighbor])
        
        # if all nodes cant be traversed 
        if len(shortest) != n:
            return -1
        else:
            return max(shortest.values())

        