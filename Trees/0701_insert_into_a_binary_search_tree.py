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
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root: return TreeNode(val)
        node = TreeNode(val)
        ptr = root
        while True:
            if(ptr.val < val):
                if ptr.right:
                    ptr = ptr.right
                else:
                    ptr.right = node
                    break
            else:
                if ptr.left:
                    ptr = ptr.left
                else:
                    ptr.left = node
                    break
        return root
