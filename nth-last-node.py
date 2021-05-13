# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        new = ListNode(0, head)
        cnt = 0
        p,q = new, new
        
        
        while p.next is not None:
            if cnt >= n:
                q = q.next
            cnt+=1
            p = p.next
            
        q.next = q.next.next
        return new.next