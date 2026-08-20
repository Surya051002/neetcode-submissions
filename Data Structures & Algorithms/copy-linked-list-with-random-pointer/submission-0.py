"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        hashmap={}
        temp=head
        ans=Node(0,None,None)
        temp2=ans
        count=0
        while temp:
            t=Node(temp.val,temp.next)
            temp2.next=t
            hashmap[count]=temp.random

            count+=1
            temp2=temp2.next
            temp=temp.next
        temp=ans.next
        temp1=head
        count=0
        # print(hashmap)
        while temp:
            hashmap[temp1]=temp
            temp1=temp1.next
            count+=1
            temp=temp.next
        temp=ans.next
        count=0
        # print(hashmap)
        while temp:
            # print(hashmap[count])
            if hashmap[count] is not None:
                temp.random=hashmap[hashmap[count]]
            else:
                temp.random=None
            temp=temp.next
            count+=1
            

        
        return ans.next

        