class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result_map = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for c in s:
                val = ord(c) - ord('a')
                counts[val]+=1
            result_map[tuple(counts)].append(s)
        
        return list(result_map.values())