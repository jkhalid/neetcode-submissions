class Solution:
    def countBits(self, n: int) -> List[int]:
        
        result = []
        for i in range(n+1):
            temp = 0
            while i!=0:
                temp += i%2
                i = i >> 1
            result.append(temp)
        return result
                
