# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        ans=True
        def fun(root,count):
            nonlocal ans
            if root is None:
                return count
            left=fun(root.left,count+1)
            right=fun(root.right,count+1)

            ans= ans and True if abs(left-right)<=1 else False
            return max(left,right)

        fun(root,0)
        return ans

        