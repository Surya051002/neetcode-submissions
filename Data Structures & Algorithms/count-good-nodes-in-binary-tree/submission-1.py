# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack=[root]
        visited=[root.val]
        ans=0
        while len(stack)>0:
            node=stack.pop()
            good=visited.pop()

            if good<=node.val:
                ans+=1
            if node.left:
                stack.append(node.left)
                if good >node.left.val:
                    visited.append(good)
                else:
                    visited.append(node.left.val)
            if node.right:
                stack.append(node.right)
                if good >node.right.val:
                    visited.append(good)
                else:
                    visited.append(node.right.val)
        return ans



        