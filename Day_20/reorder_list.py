'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

 Example : Given 1->2->3->4, reorder it to 1->4->2->3.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = []
        temp = head
        if not head:
            return None
        while temp:
            l.append(temp)
            temp = temp.next
        start = 0
        end = len(l)-1
        
        while start < end:
            l[start].next = l[end]
            l[end].next = l[start+1]
            start +=1
            end -=1
            
        if len(l)%2 ==0:
            l[start].next = None
        else:
            l[end].next = None
        return head
        