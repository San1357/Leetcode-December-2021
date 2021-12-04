#Problem no.: 322
#Problem name : Coin change

#Approach : Bottom-up 

#time : O(S*n)
#space :: O(S)

#Code : 


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        print(dp)
        dp[0] = 0
        print(dp)
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1 
