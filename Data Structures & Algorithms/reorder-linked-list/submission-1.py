# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count=0
        temp=head
        
        while temp is not None:
            count+=1
            temp=temp.next
        if count==1:
            return 
        mid=math.ceil(count/2)

        temp=head
        pre=None
        while mid>0:
            pre=temp
            temp=temp.next
            mid-=1
        newhead=None
        pre.next=None
        while temp is not None:
            t=temp
            temp=temp.next
            t.next=newhead
            newhead=t
            # print(newhead.val)


        mid=count//2

        temp1=head
        temp2=newhead
        pre=None
        while temp1 is not None and temp2 is not None:
            t=temp1
            temp1=temp1.next
            t.next=temp2
            temp2=temp2.next
            t.next.next=None
            if pre is None:
                pre=t
            else:
                while pre.next is not None:
                    pre=pre.next
                pre.next=t

        if temp1 is not None:
            while pre.next is not None:
                pre=pre.next
            pre.next=temp1
        if temp2 is not None:
            while pre.next is not None:
                pre=pre.next
            pre.next=temp2
        