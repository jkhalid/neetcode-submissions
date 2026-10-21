class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for s in strs:
            check = [0] * 26
            for char in s:
                val = ord(char) - ord('a')
                check[val]+=1
            
            result[tuple(check)].append(s)
        return list(result.values())
        