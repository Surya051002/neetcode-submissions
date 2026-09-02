# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def findk(head,k):
            while head and k>1:
                head=head.next
                k-=1
            return head
        
        def reverseList(head,k):
            pre=None
            cur=head
            while cur:
                # print(cur.val)
                node=cur.next
                cur.next=pre
                pre=cur
                cur=node
            
            return pre

        

        temp=head
        pre=None
        while temp:
            tailnode=findk(temp,k)
            # print(tailnode.val)
            if tailnode is None:
                if pre:
                    pre.next=temp
                return head
            nextNode=tailnode.next
            tailnode.next=None
            reversehead=reverseList(temp,k)
            if pre is None:
                pre=temp
            else:
                pre.next=reversehead
                pre=temp
            if temp == head:
                head=reversehead
            temp=nextNode

        return head

        


