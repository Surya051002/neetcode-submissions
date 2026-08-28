# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack=[root]
        res=[]
        v=[False]

        while stack:
            cur,vis=stack.pop(),v.pop()

            if cur:
                if vis:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    stack.append(cur.right)
                    stack.append(cur.left)
                    v.append(True)
                    v.append(False)
                    v.append(False)
            
        return res


        