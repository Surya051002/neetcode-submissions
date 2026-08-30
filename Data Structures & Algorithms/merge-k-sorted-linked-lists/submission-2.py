# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        def merge(list1,list2):
            temp1=list1
            temp2=list2
            head=ListNode(0)
            cur=head
            while temp1 and temp2:
                if temp1.val<temp2.val:
                    node=temp1
                    temp1=temp1.next
                    node.next=None
                    cur.next=node
                    cur=cur.next
                else:
                    node=temp2
                    temp2=temp2.next
                    node.next=None
                    cur.next=node
                    cur=cur.next
            if temp1 is not None:
                cur.next=temp1
            if temp2 is not None:
                cur.next=temp2
            return head.next

        while len(lists)>1:
            templist=[]
            for i in range(1,len(lists),2):
                templist.append(merge(lists[i-1],lists[i]))
            if len(lists)%2!=0:
                templist.append(lists[-1])
            lists=templist
        if lists[0] is None:
            return 
        return lists[0]
                

        