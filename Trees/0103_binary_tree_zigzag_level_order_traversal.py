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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return root
        global_list = []
        level = []
        stack = [root]
        right = False
        while len(stack) > 0:
            level = []
            temp_stack = []
            for l in range(len(stack)):
                node = stack.pop()
                level.append(node.val)

                if right:
                    if node.right is not None:
                        temp_stack.append(node.right)
                    if node.left is not None:
                        temp_stack.append(node.left)
                else:
                    if node.left is not None:
                        temp_stack.append(node.left)
                    if node.right is not None:
                        temp_stack.append(node.right)
            right^=True
            stack = temp_stack
            global_list.append(level)
        return global_list
