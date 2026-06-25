class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result_map = defaultdict(list)

        for word in strs:
            freq = [0] * 26
            for char in word:
                val = ord(char) - ord('a')
                freq[val]+=1
            result_map[tuple(freq)].append(word)
        return list(result_map.values())
        