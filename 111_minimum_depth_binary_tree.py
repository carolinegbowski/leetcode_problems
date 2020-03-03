"""
111. Minimum Depth of Binary Tree
Easy

1059

596

Add to List

Share
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0 
        else: 
            left = 1 + self.minDepth(root.left)
            right = 1 + self.minDepth(root.right)
            if left == 1:
                return right
            elif right == 1: 
                return left
            else: 
                return min(left, right)