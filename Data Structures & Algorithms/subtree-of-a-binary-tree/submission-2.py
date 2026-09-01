# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans=False

        def sameTree(root1,root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            if root1.val==root2.val:
                return sameTree(root1.left,root2.left) and sameTree(root1.right,root2.right)
            return False
        ans=False
        def dfs(root1,root2):
            nonlocal ans
            if ans:
                return ans
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            if root1.val==root2.val:
                if sameTree(root1,root2):
                    ans=True
                    return ans
            dfs(root1.left,root2)
            dfs(root1.right,root2)
        dfs(root,subRoot)
        return ans
