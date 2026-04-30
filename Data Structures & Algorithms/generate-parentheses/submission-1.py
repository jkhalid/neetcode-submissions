class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def dfs(openP, closedP, s):
            if openP == closedP and openP + closedP == 2 * n:
                result.append(s)
                return
            
            if openP < n:
                dfs(openP+1, closedP, s + '(')
            
            if closedP < openP:
                dfs(openP, closedP+1, s+ ')')

        dfs(0, 0, "")
        return result     