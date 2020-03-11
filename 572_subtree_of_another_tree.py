"""

572. Subtree of Another Tree
Easy

1862

87

Add to List

Share
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s, t):
    #should see if trees match
    #if not, recursively call matching trees...
    #on tree.left / tree.right and S
        if not t: 
            return True
        if not s: 
            return False
        if self.matchingTrees(s,t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    #should check if t OR s is None, return False
    #should check if t and s are both none, return true 
    #else: should return some version of ... 
    #calling it on the left, and calling it on the right
    #need to figure out what the return should be based on base case returns
    def matchingTrees(self, s, t):
        if not s and not t: 
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.matchingTrees(s.left, t.left) & self.matchingTrees(s.right, t.right)
        
        
        
        
        
        
        
#         if not t: 
#             return True
#         if not s: 
#             return False
#         if self.isSametree(s,t): 
#             return True
#         return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
#     def isSametree(self, s, t):
#         if not s and not t:
#             return True
#         if not s or not t:
#             return False
#         if s.val!=t.val:
#             return False
#         return self.isSametree(s.left,t.left) & self.isSametree(s.right,t.right)    