###########################################################################
#                                                                         #
# Author: Daniel Mock                                                     #
#                                                                         #
# Purpose: To document progress in learning algorithms & data structures  #
#                                                                         #
# References: This question was generated by leetcode.com. The solution   #
# to the question was generated by Daniel Mock.                           #
#                                                                         #
###########################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:return 0
        val = [0]
        return self.recurse(root, val)

    def recurse(self, root, val):
        if root:
            if root.left and not root.left.left and not root.left.right:
                val[0] += root.left.val
            self.recurse(root.left, val)
            self.recurse(root.right, val)
            return val[0]
