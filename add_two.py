# Definition for singly-linked list.
    
#class ListNode:
#    def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
class Solution:     
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:        
        head = ListNode(0)
        iterator = head

        carry = 0
        while l1 or l2 or carry:
            a1 = l1.val if l1 else 0
            a2 = l2.val if l2 else 0
            ans = a1 + a2 + carry
                
            carry = math.floor(ans/10)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
           
            iterator.next =  ListNode(ans % 10)
            iterator = iterator.next
            
        return head.next
            
    
    
        
        