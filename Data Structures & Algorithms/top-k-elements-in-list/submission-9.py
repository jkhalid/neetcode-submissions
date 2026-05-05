class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)
        max_heap = []
        for key, value in counts.items():
            heapq.heappush(max_heap, (-value, key))
        
        result = []
        while k > 0:
            value, key = heapq.heappop(max_heap)
            result.append(key)
            k-=1
        return result
        


