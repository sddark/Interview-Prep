class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head, prev = None):
        prev = None
        current = head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
            
        return prev