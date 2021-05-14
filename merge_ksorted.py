# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = len(lists)
        a = ListNode(None)
        curr = a
        q = PriorityQueue(maxsize=l)
        
        for idx, node in enumerate(lists):
            if node: q.put((node.val, idx, node))
                
        while q.qsize()>0:
            poped = q.get()
            curr.next, idx = poped[2], poped[1]
            curr = curr.next
            if curr.next: q.put((curr.next.val, idx, curr.next))
                
        return a.next
                    
            
        