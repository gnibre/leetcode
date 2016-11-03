# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


"""

!!!! AS a python export, should know htat,

variable name should not be the same as function name.
don't use peek as var


# 
it.next() may still return values, when  it.hasNext()  return False.

"""




class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator

        if self.iterator.hasNext():
            self.p = self.iterator.next()
        else:
            self.p = None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.p
        

    def next(self):
        """
        :rtype: int
        """
        # print "next"
        ret = self.p
        if self.iterator.hasNext():
            self.p = self.iterator.next()
        else:
            self.p = None
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.p is not None:
            return True
        return False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

nums = [1,34,5,7,76,989,3221,90,90,4353,4]
nums = [1,2,3,4]
it = iter(nums)
pi = PeekingIterator(it)

# print " go"
# while pi.hasNext():
#     # print "p: "
#     # print "pi"
#     print pi.peek()
#     # print " wtf"
#     # print " pi"

#     val = pi.peek()
#     # print " %r " % val
#     pi.next()

# pi.hasNext()
# pi.peek()

pi.peek()
pi.peek()
pi.next()

pi.next() #2

pi.peek() #3
pi.peek()
pi.next()

pi.hasNext()
pi.peek()
pi.hasNext()
pi.next()

print pi.hasNext()







