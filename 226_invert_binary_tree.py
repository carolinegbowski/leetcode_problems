"""

226. Invert Binary Tree
Easy

2566

41

Add to List

Share
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# [4,2,7,1,3,6,9]


class Solution:
    def invertTree(self, root):    
        if not root: 
            return None
        else: 
            right = self.invertTree(root.right)
            left = self.invertTree(root.left)
            root.left = right
            root.right = left
            return root
        
