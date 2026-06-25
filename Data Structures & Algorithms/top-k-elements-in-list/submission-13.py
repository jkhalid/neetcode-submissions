class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        freq = [[] for i in range(n+1)]

        counts = Counter(nums)

        for key,fq in counts.items():
            freq[fq].append(key)
        result = []
        while n > 0:
            for num in freq[n]:
                if k == 0:
                    break
                result.append(num)
                k-=1
            n-=1
        return result
