

#Problem :cyclically rotate_arrayby 1
#time:O(n)
#space: O(1)

#Code;

def rotate(arr, n):
    i = 0
    j = n - 1
    while i != j:
      arr[i], arr[j] = arr[j], arr[i]
      i = i + 1
    
        
print(rotate([1,2,3,4,5], 5))
