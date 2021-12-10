
#problem no. : 790
#problem name : Domino and Tromino Tiling

#time : O(N)

#space : O(1)

#code : 



class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007
        if n <= 2:
            return n
        fPrevious = 1
        fCurrent = 2
        pCurrent = 1
        for k in range(3, n + 1):
            tmp = fCurrent
            fCurrent = (fCurrent + fPrevious + 2 * pCurrent) % MOD
            pCurrent = (pCurrent + fPrevious) % MOD
            fPrevious = tmp
        return fCurrent
