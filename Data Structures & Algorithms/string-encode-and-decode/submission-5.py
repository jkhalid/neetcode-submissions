class Solution:

    def encode(self, strs: List[str]) -> str:

        result = []

        for string in strs:
            temp = str(len(string))+'#'+string
            result.append(temp)
        
        return ''.join(result)


    def decode(self, s: str) -> List[str]:

        result = []
        n = len(s)
        i = 0

        while i < n:
            start = i
            end = start

            while s[end] != '#':
                end+=1
            
            length = int(s[start:end])
            word_start = end+1
            word_end = word_start+length

            word = s[word_start:word_end]
            result.append(word)
            i = word_end
        
        return result

