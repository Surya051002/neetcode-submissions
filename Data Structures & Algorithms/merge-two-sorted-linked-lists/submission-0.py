# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        if list2 is None:
            return list1
        temp=None
        newhead=None

        while list1 is not None and list2 is not None:
            
            if(list1.val<list2.val):
                
                if temp is not None:
                    temp.next=list1
                    temp=temp.next
                else:
                    temp=list1
                    newhead=temp
                
                list1=list1.next
            else:
                if temp is not None:
                    temp.next=list2
                    temp=temp.next
                else:
                    temp=list2
                    newhead=temp
                list2=list2.next
        if list1 is not None:
            temp.next=list1
        if list2 is not None:
            temp.next=list2
        return newhead
        