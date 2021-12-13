
#Problem no. : 698
#Problem name : Partition to K Equal Sum Subsets
#time : O(N*(2^n))
# SPace : O(2^n)



#code:

class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        total_array_sum = sum(arr)
        n = len(arr)
        
        # If the total sum is not divisible by k, we can't make subsets.
        if total_array_sum % k != 0:
            return False

        target_sum = total_array_sum // k

        subsetSum = [-1] * (1 << n)
        #print("subsetSum:", subsetSum)
        # Initially only one state is valid, i.e don't pick anything
        subsetSum[0] = 0
        #print("subsetSum:", subsetSum)
        
        for mask in range(1 << n):
            # If the current state has not been reached earlier.
            if subsetSum[mask] == -1: 
                continue

            for i in range(n):
                # If the number arr[i] was not picked earlier, and arr[i] + subsetSum[mask]
                # is not greater than the targetSum then add arr[i] to the subset
                # sum at subsetSum[mask] and store the result at subsetSum[mask | (1 << i)].
                if (mask & (1 << i)) == 0 and subsetSum[mask] + arr[i] <= target_sum: 
                    subsetSum[mask | (1 << i)] = (subsetSum[mask] + arr[i]) % target_sum
                
            if subsetSum[-1] == 0: 
                return True 
            
        return subsetSum[-1] == 0
