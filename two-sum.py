
#probllem name: Twosum
 
 #OPTImISE SOLutION 

#time : O(n)
#space : O(n)


#Code :

#Approach : using hashmap 

class Solution:
  def twoSum(self, nums: List[int], target : int) -> List[int]:
    hashmap = {}      # Space : O(n)
    
    for i in range(len(nums)):  # time : O(n)
      hashmap[nums[i]] = i      # O(1)
    print("hashmap:", hashmap)  # O(1)
    
    
    for i in range(len(nums)):  #time  O(n)
      x_value = target - nums[i]  #O(1)
      
      if x_value in hashmap and hashmap[x_value] != i:  #O(1)
        return [i, hashmap[x_value]]   
                   
