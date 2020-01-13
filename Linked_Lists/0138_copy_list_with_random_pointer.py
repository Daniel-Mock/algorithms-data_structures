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

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node = head

        cache = {None:None}

        while node:
            if node not in cache:
                cache[node] = Node(node.val)

            if node.next not in cache:
                cache[node.next] = Node(node.next.val)
            cache[node].next = cache[node.next]

            if node.random not in cache:
                cache[node.random] = Node(node.random.val)
            cache[node].random = cache[node.random]

            node = node.next
        return cache[head]

        '''if head is None: return head
        node = head
        dummy = Node(0,0,0)
        random_list = []
        lst = dummy

        while node is not None:
            new_node = Node(node.val, None, None)
            lst.next = new_node
            if node.random is None:
                random_list.append(None)
            else: random_list.append(node.random.val)
            lst = lst.next
            node = node.next

        lst = dummy.next
        while lst is not None:
            print(lst.val, lst.next, lst.random)
            lst = lst.next
        print(len(random_list))
        print(random_list)

        lst = dummy.next
        ref = dummy.next
        while len(random_list) > 0:
            rand_node = random_list.pop(0)
            if rand_node is None:
                pass
            else:
                while lst is not None:
                    if rand_node == lst.val:
                        ref.random = lst
                    lst = lst.next
            lst = dummy.next
            ref = ref.next
        return dummy.next
        '''




        #################################################



        '''node = head

        nodes = {}
        random = {}

        while node is not None:
            new_node = Node(node.val, node.next, node.random)
            if node is head:
                head_ref = new_node

            if new_node.next is None: pass
            elif new_node.next not in nodes:
                node_ref = new_node.next
                new_node2 = Node(node_ref.val, node_ref.next, node_ref.random)
                new_node.next = new_node2
                nodes[new_node2] = new_node2

            if new_node.random is None: pass
            elif new_node.random not in nodes:
                node_ref = new_node.random
                new_node2 = Node(node_ref.val, node_ref.random, node_ref.random)
                new_node.random = new_node2
                nodes[new_node2] = new_node2

            node = node.next
        #return head_ref
        '''    