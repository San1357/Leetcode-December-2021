
#Problem name :Sort an arrays of 0s,1s & 2s.
#time: O(n)
#space:O(1)

#Code:
def Sort012(arr):
  n = len(arr)
  cnt0 = 0
  cnt1 = 0
  cnt2 = 0
  
  for i in range(n):
    if arr[i] == 0:
      cnt0 += 1
    elif arr[i] == 1:
      cnt1 += 1
    elif arr[i] == 2:
      cnt2 +=1
      
  i= 0
  while cnt0>0:
    arr[i] = 0
    i+=1
    cnt0 -=1
    
  while cnt1 > 0:
    arr[i] = 1
    cnt1-=1
    i+=1
    
  while cnt2>0:
    arr[i] = 2
    i+=1
    cnt2-=1
    
  return arr
