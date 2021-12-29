



#Problem no: 116

#Problem name: Populating Next Right Pointers in Each Node

#time: O(N)
#space: O(1)

#Code:

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        
        leftmost = root
        
        while leftmost.left:
            
            
            head = leftmost
            while head:
                
                head.left.next = head.right
                
                if head.next:
                    head.right.next = head.next.left
                
                head = head.next
            
            leftmost = leftmost.left
        
        return root 
      
      

