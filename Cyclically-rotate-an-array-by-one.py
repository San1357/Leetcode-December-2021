
#Problem name: Cyclically rotate an array by one

#time : O(n)
#space: O(1)


#Code:

def cyclically_Rotate(arr):
  
  x = arr[-1]
  
  for i in range(n-1,0,-1):
    arr[i] = arr[i-1]
  arr[0] = x
  print(arr)
  return arr

cyclically_Rotate([1,2,3,4,5])
