# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        l = []
        for v in self.iit(root):
            l.append(v)
        return l
        # return [v for v in self.iit(root)]
    
    # ignore left in order transfer
    def iit(self,root):
        if root is None:
            return
        yield root.val
        for r in self.iit(root.right):
            yield r

        




# test generator
def tg(i):
    print "-> tg, %d" % i

    yield i

    if i < 0:
        return

    if i%2==0:
        yield i/2

    if i%3==0:
        yield i/3


    for r in tg(i-1):
        yield r




tl = [v for v in tg(10)]


print tl