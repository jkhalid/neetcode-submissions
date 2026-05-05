class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # bucket sort 

        counts = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        for key, fq in counts.items():
            freq[fq].append(key)

        n = len(nums) -1
        result = []
        while k > 0:
            if len(freq[n]) > 0:
                for num in freq[n]:
                    result.append(num)
                    k-=1
            n-=1
        
        return result        