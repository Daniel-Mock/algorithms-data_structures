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
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        if l1 is None and l2 is None:
            return
        stack_1 = []
        stack_2 = []
        carry = False
        sum_vals = []
        while l1 is not None:
            stack_1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            stack_2.append(l2.val)
            l2 = l2.next
        for _ in range(min(len(stack_1),len(stack_2))):
            num_1 = stack_1.pop()
            num_2 = stack_2.pop()
            #print(f"num_1: {num_1}, num_2: {num_2}")
            if carry == True:
                num_1 +=1
            val = num_1 + num_2
            if val >= 10:
                carry = True
                val -= 10
            else:
                carry = False
            sum_vals.append(val)

        if len(stack_1) > 0:
            for val in reversed(stack_1):
                if carry == True:
                    val+=1
                    carry = False
                if val >= 10:
                    carry = True
                    val -= 10
                sum_vals.append(val)

        elif len(stack_2) > 0:
            for val in reversed(stack_2):
                if carry == True:
                    val+=1
                    carry = False
                if val >= 10:
                    carry = True
                    val -= 10
                sum_vals.append(val)
        if carry == True:
            sum_vals.append(1)
        head_ref = ListNode(val=sum_vals.pop())
        node = head_ref
        #test
        for _ in range(len(sum_vals)):
            lst_val = sum_vals.pop()
            node.next = ListNode(val=lst_val)
            node = node.next

        return head_ref