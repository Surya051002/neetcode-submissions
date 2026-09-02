# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        lists=[root]
        ans=[]

        while len(lists)>0:
            templist=[]
            ans.append(lists[-1].val)
            while len(lists)>0:
                node=lists.pop(0)
                if node.left:
                    templist.append(node.left)
                if node.right:
                    templist.append(node.right)
            lists=templist
        return ans
            

