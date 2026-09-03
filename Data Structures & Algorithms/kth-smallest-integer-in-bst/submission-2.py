# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        cur=root
        count=0
        arr=[]
        while cur:
            
            if cur.left is None:
                count+=1
                arr.append(cur.val)
                if count==k and cur:
                    return cur.val
                cur=cur.right
            else:
                temp=cur.left
                while temp.right and temp.right!=cur:
                    temp=temp.right
                if temp.right is None:
                    temp.right=cur
                    cur=cur.left
                else:
                    count+=1
                    arr.append(cur.val)
                    if count==k and cur:
                        return cur.val
                    temp.right=None
                    cur=cur.right
            # print(count,cur.val)
            
        return 0


