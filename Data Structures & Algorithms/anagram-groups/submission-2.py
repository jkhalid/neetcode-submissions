class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_map = defaultdict(list)

        for s in strs:
            sorted_string = ''.join(sorted(s))
            sorted_map[sorted_string].append(s)
        return list(sorted_map.values())

        


        

        
            

        