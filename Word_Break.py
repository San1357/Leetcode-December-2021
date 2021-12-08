# Problem no. : 139 
# Problem name : Word_Break 

#time : O(n^3) # because of substring caculating at every iteration.


#CODE :


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        print("wordDict:", wordDict)
        
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        print("dp:", dp)
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
                    
        print(dp[len(s)])
        return dp[len(s)]
      
      
