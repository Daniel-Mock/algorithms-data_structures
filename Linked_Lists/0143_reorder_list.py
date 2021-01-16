class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #create list of nodes
        #separate list into 2 lists, Left & Right side
        #iterate through (# nodes)/2, pop node from end of 2nd list and insert into
            #first list at (current position + 1)
        #iterate through new list and set node.next = next item in list

        if not head: return
        if head.next is None: return head
        if head.next.next is None: return

        #Step 1: Populate list of nodes
        lst = []
        while head:
            lst.append(head)
            head = head.next
        len_lst = len(lst)

        #Step 2: Find midpoint
        if len_lst % 2 == 0:
            mid = len_lst //2
        else:
            mid = (len_lst //2) + 1

        #Step 3: Split list into Left & Right lists
        list_right = lst[mid:]
        list_left = lst[:mid]

        #Step 4: Iterate through (length of lst/2), pop from list right
            #and append to list left
        pos = 0
        for _ in range(len(list_right)):
            list_left.insert(pos+1, list_right.pop())
            pos+=2

        #Step 5:Iterate through full list and set new links
        for index, val in enumerate(list_left[:-1]):
            val.next = list_left[index+1]
        list_left[-1].next = None
            
