
#Problem name: Intersection of two arrays

#time: O(m+n)
#Space:O(n)

#Code:

def intersectionarr(arr,arr2):
    i = 0
    j = 0
    res = []
    m = len(arr)
    n = len(arr2)
    
    while i < m and j < n:
        if arr[i]<arr2[j]:
            
            i+=1
            
        elif arr2[j]<arr[i]:
           
            j+=1
            
        else:
            res.append(arr2[j])
            i+=1
            j+=1
    return res
    
print(intersectionarr([1,3,5,7,8],[2,4,6,8]))
