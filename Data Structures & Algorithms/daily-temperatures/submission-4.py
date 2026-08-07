class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp,index = stack.pop()
                result[index] = i - index
            stack.append((t,i))
        return result