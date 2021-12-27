

#Problem no: 476
#problem name: Number Complement
#time: O(1).
#space: O(1).



#Code:


class Solution:
    def findComplement(self, num):
        bitmask = num
        bitmask |= (bitmask >> 1)
        bitmask |= (bitmask >> 2)
        bitmask |= (bitmask >> 4)
        bitmask |= (bitmask >> 8)
        bitmask |= (bitmask >> 16)
        
        return bitmask ^ num
