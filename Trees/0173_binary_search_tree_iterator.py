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

#Time complexity: Creating list = O(N). Returning next smallest node: O(1)

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.lst = []
        stack = []
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left

            elif stack:
                node = stack.pop()
                self.lst.append(node.val)
                node = node.right
            else: break



    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.lst.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.lst): return True
        else: return False
