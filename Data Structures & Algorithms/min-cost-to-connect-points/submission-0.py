class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        adj = {i : [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([j, dist])
                adj[j].append([i, dist])
        
        visited = set()
        visited.add(0)
        mst = [(0,0)]
        min_heap = []

        for dst, dist in adj[0]:
            heapq.heappush(min_heap, [dist, 0, dst])
        
        while min_heap:
            d , u, v = heapq.heappop(min_heap)
            if v in visited:
                continue
            visited.add(v)
            mst.append((v,d))

            for nei, dist in adj[v]:
                if nei not in visited:
                    heapq.heappush(min_heap, [dist, v, nei])
        result = 0
        for edge in mst:
            node , dist = edge
            result += dist
        return result

        