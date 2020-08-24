# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
DFS approach (either Inorder, Preorder or Postorder)
and checking if the Left Child is a Leaf node.
 If it is, then add the nodes value to the sum variable

'''
class Solution:
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right:   #to check if it is a leaf
                if is_left:
                    return node.val
                return 0
            return dfs(node.left, True) + dfs(node.right, False)
        
        return dfs(root, False)