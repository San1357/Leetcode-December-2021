# Problem no:  876
# Problem name : Middle of the Linked List  

#time: O(n)
#space: O(1)
#code :


class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
