
#PRoblem no :231
#PRoblem name : Power of Two


#time : O(1)
#Space complexity : O(1)


#Code:

class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (-n) == n
