# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap={}
        for key,value in enumerate(inorder):
            hashmap[value]=key
        index=0
        
        def createTree(preorder,leftinorder,rightinorder):
            nonlocal index

            if leftinorder>rightinorder:
                return None
            root=TreeNode(preorder[index])
            mid=hashmap[preorder[index]]
            index+=1

            root.left=createTree(preorder,leftinorder,mid-1)
            root.right=createTree(preorder,mid+1,rightinorder)

            return root
        return createTree(preorder,0,len(preorder)-1)
            
        