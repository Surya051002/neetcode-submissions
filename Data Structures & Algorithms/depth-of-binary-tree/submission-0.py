# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        length=0
        ans=0
        
        
        def fun(root,length):
            nonlocal ans
            if root is None:
                return
            length+=1
            ans=max(ans,length)
            fun(root.left,length)
            fun(root.right,length)
            length-=1
        fun(root,length)
        return ans


        