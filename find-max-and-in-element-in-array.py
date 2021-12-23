#approach1: optimise than approach2

#time :O(n)
#space :O(1)
#CODE :

def find_min_max(array):
  n = length(array)
  if n % 2==0:
    if array[0]>array[1]:
      _max = array[0]
      _min = array[1]
    
    else:
      _max = array[1]
      _min = array[0]
      i= 2 
  else:
    _max = array[0]
    _min = array[0]
    
  while i<n-1:
    if array[i]>array[i+1]:
      if array[i]>_max:
        _max = array[i]
      if array[i+1]<_min:
        _min = array[i+1]
    
    elif array[i+1]>array[i]:
      if  array[i+1]>_max:
        _max = array[i+1]
      if array[i] <_min:
        _min = array[i]
        
  return _min,_max

#Appraoch 2
    
#Code :
#time :O(n)
#Space : O(1)

def findminmax(array):
    
    n = len(array)
    if len(array) == 1:
        _min = array[0]
        _max = array[0]
    else:
        if array[0]>array[1]:
            _max  = array[0]
            _min = array[1]
            
        else:
            _max = array[1]
            _min = array[0]
        for i in range(2, n):   
            if array[i] > _max:
                _max = array[i]
            elif array[i] < _min:
                _min = array[i]
        return _min,_max
    
print(findminmax([43,9,2,56,1,42]))
