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

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (not l1): return l2
        if(not l2): return l1
        if(l1.val <= l2.val):
            headPtr = l1
            l1 = l1.next
        else:
            headPtr = l2
            l2 = l2.next


        tail = headPtr
        while(l1 and l2):
            if(l1.val <= l2.val):
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next

        if(l1 and not l2):
            tail.next = l1
            l1 = l1.next

        if(l2 and not l1):
            tail.next = l2
            l2 = l2.next

        return headPtr
