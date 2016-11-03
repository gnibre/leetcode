# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head


    
    def getRandom(self):
        # Reservoir Sampling.

        # for each number we saw of index n , set chance of   1/n , to pick it.
        # as the list goes, it changes over time.


    def getRandom_really_random_function_i_wrote(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        
        l = 0
        nd = self.head
        while nd is not None:
            l+=1
            nd = nd.next
        
        r = random.randint(0,l-1)
        nd = self.head
        while r>0:
            nd = nd.next
            r-=1
        return nd.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()



