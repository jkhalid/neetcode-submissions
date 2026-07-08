class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for string in strs:
            check = [0] * 26
            for char in string:
                val = ord(char)-ord('a')
                check[val]+=1
            result[tuple(check)].append(string)
        
        return list(result.values())
        