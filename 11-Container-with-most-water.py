

#Problem no: 11
#Problem name  : Container With Most Water

# Approach 1: Brute force

# time : O(n^2)
# space : O(1)

#Code :

class Solution:
  def maxArea(self, height):
    result = 0
    for i in range(len(height)):
      for j in range(i+1, len(height)):
        width = j - i
        h = min([height[i],height[j])
        area = h*width
        result =  max(area, result)
                
    
    return result
                 
          
                 
#Approach 2: Two pointer approach
# time : O(n)
# space  : O(1)

                 

                                
#CODE:
                 
class Solution:
  def maxArea(self, height):

    result  = 0 
    i =  0
    j  = len(height)-1
    while (i<j):
        width = (j-i)
        h = min(height[i], height[j])
        area = width * h
        result = max(result,area)

        if height[i]<height[j]:
            i+=1
        else:
            j-=1
    return  result
                
 
  
                 
                 
                 
