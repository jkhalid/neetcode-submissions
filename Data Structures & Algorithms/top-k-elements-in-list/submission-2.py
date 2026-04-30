class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_counts = defaultdict(int)

        for num in nums:
            num_counts[num] +=1

        count_nums = defaultdict(list)
        for num, count in num_counts.items():
            count_nums[count].append(num)
        
        res = []

        for key in sorted(count_nums.keys(), reverse=True):
            temp = count_nums[key]
            for value in temp:
                res.append(value)
                k -= 1
                if k == 0:
                    return res
        
        return res
        

        


        

        
        