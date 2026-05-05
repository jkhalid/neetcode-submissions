class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)
        sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

        result = []
        
        for key in sorted_counts.keys():
            if k == 0:
                break
            else:
                result.append(key)
                k-=1
        return result
