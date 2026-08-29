# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDia = 0
        def DFS(node):
            nonlocal maxDia

            if not node:
                return 0

            leftHeight = DFS(node.left)
            rightHeight= DFS(node.right)

            currDia = leftHeight + rightHeight

            maxDia = max(maxDia,currDia)

            return 1+max(leftHeight,rightHeight)

        DFS(root)
        return maxDia



            

        
        