class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}

        for u,v,w in edges:
            adj[u].append([v,w])
            adj[v].append([u,w])

        visited = set()
        mst = [(0,0)]
        min_heap = []

        for neighbor , weight in adj[0]:
            heapq.heappush(min_heap, [weight, 0, neighbor])
        
        visited.add(0)

        while min_heap:
            wt ,src, dst = heapq.heappop(min_heap)

            if dst in visited:
                continue
            visited.add(dst)
            mst.append((dst,wt))

            for nei, cost in adj[dst]:
                if nei not in visited:
                    heapq.heappush(min_heap, [cost, dst, nei])
        
        if len(mst) != n:
            return -1
        result = 0
        for edge in mst:
            node , cost = edge
            result += cost
        return result


        