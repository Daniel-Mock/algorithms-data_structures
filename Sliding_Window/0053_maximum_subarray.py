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


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None: return None
        local_max_num = float("-inf")
        global_max_num = float("-inf")
        for num in nums:
            local_max_num = max(num, num + local_max_num)
            if local_max_num > global_max_num:
                global_max_num = local_max_num
        return global_max_num