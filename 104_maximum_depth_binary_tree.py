"""
104. Maximum Depth of Binary Tree
Easy

2006

66

Add to List

Share
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

Accepted
704,486
Submissions
1,099,193
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Given binary tree [3,9,20,null,null,15,7],

class Solution:
    def maxDepth(self, root):
        if not root: 
            return 0
        else:
            left = 1 + self.maxDepth(root.left)
            right = 1 + self.maxDepth(root.right)
        return max(left, right)