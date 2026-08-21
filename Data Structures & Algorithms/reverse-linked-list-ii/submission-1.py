# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        leftpoint=None
        rightpoint=None
        prepoint=None
        temp=head
        l=left
        r=right
        while left>0 or right >0:
            if left-1==1: prepoint=temp
            if left-1==0 : leftpoint=temp
            if right-1==0: rightpoint=temp
            temp=temp.next
            left-=1
            right-=1
        if prepoint:
            print(prepoint.val)
        temp=leftpoint
        newhead=None
        # print(leftpoint.val)
        while temp and l<=r:
            t=temp
            temp=temp.next
            t.next=newhead
            newhead=t
            l+=1
            # print(l)
        if prepoint is not None:
            prepoint.next=newhead
        else:
            head=newhead
        t =head
        while t.next:
            t=t.next
        t.next=temp

        return head
        
        
            
             
        
            
        