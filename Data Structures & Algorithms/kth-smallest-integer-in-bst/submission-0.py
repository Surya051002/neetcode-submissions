# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if root is None:
            return None
        count=0
        ans=-1
        def findKth(root,k):
            nonlocal count
            print(count)
            nonlocal ans
            if root is None:
                return 
            
            
            left=findKth(root.left,k)
            count+=1
            if root and count==k:
                ans=root.val
                return
            right=findKth(root.right,k)
        
        findKth(root,k)
        return ans
