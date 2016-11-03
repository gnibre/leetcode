# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        #  if have left and right, just append [lc,rc] on its turn
        #  if have left child only: L add L ,   if have right child only , append R, if have no child , append F(leaf)

        l = []
        l.append(root)

        ret = []
        for n in l:
            if n is None:
                continue

            nodecode = ""
            if n.left is not None:
                l.append(n.left)
                nodecode = "L"

            if n.right is not None:
                l.append(n.right)
                nodecode += "R"

            if len(nodecode) == 0:
                nodecode = 'F'  # leaf.
            elif len(nodecode) == 2:
                nodecode = ''

            ret.append(nodecode + str(n.val))

        # done.
        # sstr = ','.join(str(n) for n in ret)
        sstr = ','.join(ret)
        return sstr

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        l = data.split(',')

        if len(l) < 1:
            return None
        root = TreeNode(l[0])
        nl = [root]  # node list.
        p = 1
        while len(nl) > 0:
            n = nl.pop(0)
            if n.left is not None:
                nn = self.createTreeNode(l[p])
                n.left = nn
                nl.append(nn)
                p += 1
            if n.right is not None:
                nn = self.createTreeNode(l[p])
                n.right = nn
                nl.append(nn)
                p += 1
        return root

    def createTreeNode(self, sdata):
        if sdata[0] == 'L':
            n = TreeNode(int(sdata[1:]))
            n.left = TreeNode(0)
        elif sdata[0] == 'R':
            n = TreeNode(int(sdata[1:]))
            n.right = TreeNode(0)
        elif sdata[0] == 'F':
            n = TreeNode(int(sdata[1:]))
        else:
            n = TreeNode(int(sdata))
            n.left = TreeNode(0)
            n.right = TreeNode(0)
        return n

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
