class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counts = Counter(nums)
        counters = [[] for _ in range(n+1)]

        for key, value in counts.items():
            counters[value].append(key)

        result = []
        for i in range(n, -1, -1):
            for val in counters[i]:
                result.append(val)
                if len(result) == k:
                    return result
        return result
