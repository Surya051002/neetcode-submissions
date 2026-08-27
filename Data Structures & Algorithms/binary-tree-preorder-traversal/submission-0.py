# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        stack.append(root)
        ans=[]
        while len(stack)>0:
            temp=stack.pop()
            if temp is not None:
                ans.append(temp.val)
            if temp and temp.right is not None:
                stack.append(temp.right)
            if temp and temp.left is not None:
                stack.append(temp.left)
        return ans

        