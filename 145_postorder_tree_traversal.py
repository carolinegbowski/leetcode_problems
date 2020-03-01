"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# postorder = left, right, root

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.traversalHelper(root, output)
        return output
        
    def traversalHelper(self, root, output):
        if not root:
            return
        else: 
            self.traversalHelper(root.left, output)
            self.traversalHelper(root.right, output)
            output.append(root.val)
            return