
#problem no: Union_two_arrays
#time: O(m+n)
#space:O(n)

#Code:

def unionarr(arr,arr2):
    i = 0
    j = 0
    res = []
    m = len(arr)
    n = len(arr2)
    
    while i < m and j < n:
        if arr[i]<arr2[j]:
            res.append(arr[i])
            i+=1
            print(res)
        elif arr2[j]<arr[i]:
            res.append(arr2[j])
            j+=1
            print(res)
        else:
            res.append(arr2[j])
            i+=1
            j+=1
    return res
    
print(unionarr([1,3,5,7,8],[2,4,6,8]))
