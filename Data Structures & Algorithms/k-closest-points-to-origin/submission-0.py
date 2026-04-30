class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = []
        result = []

        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            heapq.heappush(min_heap, (distance, point))
        while k > 0:
            result.append(heapq.heappop(min_heap)[1])
            k -=1
        return result
        