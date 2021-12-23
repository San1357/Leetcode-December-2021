#problem no: 344
#problem name : Reverse string



#time : O(n)
#Space: O(1)
#approach : two pointer


#Code:

def reverse(s):
  start = 0
  end = len(s)-1
  while start < end:
    s[start],s[end]= s[end],s[start]
    start += 1
    end -= 1
  return s 

