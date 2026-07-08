class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for string in strs:
            val = str(len(string))+'#'+string
            encoded.append(val)
        
        return ''.join(encoded)

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
            word_start = end + 1
            word_end = word_start + length
            result.append(s[word_start:word_end])
            i = word_end


        return result

