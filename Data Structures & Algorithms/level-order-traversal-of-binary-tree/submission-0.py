# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        lists=[root]

        ans=[]

        while len(lists)>0:
            templist=[]
            tempval=[]
            while len(lists)>0:
                node=lists.pop(0)
                tempval.append(node.val)
                if node.left:
                    templist.append(node.left)
                if node.right:
                    templist.append(node.right)
            lists=templist
            ans.append(tempval)
        return ans


