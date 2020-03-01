"""
144. Binary Tree Preorder Traversal
Medium

1184

50

Add to List

Share
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# preorder == root, left, right 

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.traversalHelper(root, output)
        return output
    
    def traversalHelper(self, root, output):
        if not root: 
            return
        else: 
            output.append(root.val)
            self.traversalHelper(root.left, output)
            self.traversalHelper(root.right, output)
            