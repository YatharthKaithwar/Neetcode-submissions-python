# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def DFS(node):
            if not node:
                return 0

            leftMax = max(DFS(node.left), 0)
            rightMax = max(DFS(node.right), 0)

            self.maxSum = max(
                self.maxSum,
                node.val + leftMax + rightMax
            )

            return node.val + max(leftMax, rightMax)

        DFS(root)
        return self.maxSum