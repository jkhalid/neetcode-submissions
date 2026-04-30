class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_freq_dict = defaultdict(int)
        for num in nums:
            num_freq_dict[num] +=1
        
        freq_num_dict = defaultdict(list)

        for num , freq in num_freq_dict.items():
            freq_num_dict[freq].append(num)
        
        res = []

        for key in sorted(freq_num_dict.keys(), reverse=True):
            temp = freq_num_dict[key]
            for value in temp:
                res.append(value)
                k -= 1
                if k == 0:
                    return res
        
        return res


        

        
        