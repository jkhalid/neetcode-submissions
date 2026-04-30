class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # top down
        memo = {}

        def dfs(amt):
            if amt == 0:
                return 0
            if amt in memo:
                return memo[amt]
            
            result = 1e9
            for coin in coins:
                if amt - coin >= 0:
                    result = min(result, 1+dfs(amt-coin))
            memo[amt] = result
            return result
        
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins

        


        