class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = defaultdict(list)
        for word in strs:
            sorted_word = sorted(word)
            sorted_word_joined = ''.join(sorted_word)
            result_map[sorted_word_joined].append(word)
        
        result = []
        for values in result_map.values():
            result.append(values)
        return result