
# problem no.: 1217
# problem name:  Minimum Cost to Move Chips to The Same Position
# Time : O(N)
# space : O(1) 


# code:

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_cnt = 0
        odd_cnt = 0
        for i in position:
            if i % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
        return min(even_cnt, odd_cnt)
