# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        temp=head

        while temp:
            count+=1
            temp=temp.next
        count=count-n
        
        if count ==0:
            return head.next
        temp=head
         
        while count>1:
            count-=1
            temp=temp.next
        print(count,temp.val)
        temp.next=temp.next.next

        return head
        
        

        