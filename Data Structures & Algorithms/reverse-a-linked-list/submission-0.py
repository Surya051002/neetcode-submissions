# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        newhead=None

        while head is not None:

            temp=head
            head=head.next
            temp.next=newhead
            newhead=temp
        return newhead