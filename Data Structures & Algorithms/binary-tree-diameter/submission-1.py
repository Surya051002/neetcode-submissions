# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def fun(root,count,leftmax):
            nonlocal ans
            if root is None:
                return 0
            
            left=fun(root.left,count+1,leftmax)
            right=fun(root.right,count+1,leftmax)
            ans=max(ans,left+right)
            return 1+max(left,right)
        fun(root,0,0)
        return ans
            

        