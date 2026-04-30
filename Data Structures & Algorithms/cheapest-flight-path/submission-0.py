class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = {i:[] for i in range(n)}
        for u, v, price in flights:
            adj[u].append([v, price]) 

        prices = [float("inf")] * n
        prices[src] = 0
        q = deque([(0, src, 0)])

        while q:
            cost , node , stops = q.popleft()
            if stops > k:
                continue

            for nei, w in adj[node]:
                nextCost = cost + w
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    q.append((nextCost, nei, stops + 1))

        return prices[dst] if prices[dst] != float("inf") else -1      

        