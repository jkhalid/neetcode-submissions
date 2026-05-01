class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result_map = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            result_map[sorted_s].append(s)
        result = []
        for r in result_map.values():
            result.append(r)
        return result