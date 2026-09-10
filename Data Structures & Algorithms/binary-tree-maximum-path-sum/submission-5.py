class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(root):
            nonlocal max_sum
            if root is None:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)

            max_sum=max(max_sum,root.val+left+right,root.val,root.val+left,root.val+right)

            return max(root.val,root.val+left,root.val+right)




           
        dfs(root)
        return max_sum