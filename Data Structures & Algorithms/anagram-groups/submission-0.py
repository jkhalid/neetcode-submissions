class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        string_map = defaultdict(list)
        for s in strs:
            sorted_string = ''.join(sorted(s))
            string_map[sorted_string].append(s)

        result = []
        for values in string_map.values():
            result.append(values)
        return result

        
            

        