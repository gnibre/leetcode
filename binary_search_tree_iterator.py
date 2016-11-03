# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.r = root
        self.p = []
        self.buildMinPath(self.r)

    
    def buildMinPath(self, nd):
        while nd is not None:
            self.p.append(nd)
            nd = nd.left
    
    def hasNext(self):
        """
        :rtype: bool
        """
        
        if len(self.p)==0:
            return False
        return True

    def next(self):
        """
        :rtype: int
        """
        if len(self.p)==0:
            return None
        print " working on next. "
        nd = self.p[-1]
        ret = nd.val
        
        print "ret get already : %d " % ret
        # before return, move p to next.
        
        # have right child.  find smallest in set right child.
        # no right child?. parent is next. which is in the path.
        
        if nd.right is not None:
            print " going right"
            self.buildMinPath(nd.right)
        else:
            print " dealing with parents"
            print " cur:  %r " % self.p
            # mistake made. 
            # pop til get something bigger.
            self.p.pop()
            print " pop: %r " % self.p
            while len(self.p)>0:
                if self.p[-1].val < ret:
                    self.p.pop()
                else:
                    break
            print " get it done : %r " % self.p
        return ret

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


root = TreeNode(2)
nd1 = TreeNode(1)
root.left = nd1


bi = BSTIterator(root)


print bi.hasNext()
print bi.next()
print bi.hasNext()
print bi.next()
print bi.hasNext()


