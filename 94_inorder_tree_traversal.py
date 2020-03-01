"""
94. Binary Tree Inorder Traversal
Medium

2504

105

Add to List

Share
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# inorder == left, root, right

"""


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.traversalHelper(root, output)
        return output
        
    def traversalHelper(self, root, output):
        if not root:
            return
        else: 
            self.traversalHelper(root.left, output)
            output.append(root.val)
            self.traversalHelper(root.right, output)
            return