
class LTreeNode(object):
    def __init__(self, lv, parent_length, name):
        self.level = lv
        self.name = name
        self.length = parent_length + len(name)
        if lv > 1:
            self.length += 1  # / after parent path
        self.cl = []

    def add_child(self, name):

        child = LTreeNode(self.level + 1, self.length, name)
        self.cl.append(child)
        return child


class Solution(object):

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        # input is -> tree tranverse. preorder, self -> leftc(expand c), other c, all c, right most c,

        #  find  token \n ->  ready for next token to be folder or file, with level
        #  find  \t{m} level of the file is m.  (m=0) root.
        #        if current we are working on a treenode with level 1.
        #        when m <=1, we switch current folder to the comming folder
        #        if  m - currentlevel>1, error.  but we don't check that i think.
        #
        #  find folder-> add to tree;  current node.
        #  find file -> add to tree, current node. and also calc lenght;

        #
        if input is None:
            return 0
        folders = input.split("\n")
        if len(folders) == 0:
            return 0

        #  root is virtual. coming input is all under root, except they dont came after
        #  which means the first folder given is not 'root' and there might be other folders at teh same level as the first folder.
        root = LTreeNode(0, 0, "")
        # root = LTreeNode(0, 0, folders[0])
        path = [root]
        maxLength = root.length
        # cur_node = root
        for f in folders:
            level = 0
            while f[0] == '\t':
                level += 1
                f = f[1:]
            # error if invalid string get.
            path = path[:level + 1]
            parent_node = path[-1]
            child = parent_node.add_child(f)
            path.append(child)

            if "." in f:
                # file.
                pathlength = child.length
                if pathlength > maxLength:
                    for p in path:
                        print p.name
                maxLength = maxLength if maxLength > pathlength else pathlength

        return maxLength


s = Solution()
s1 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
s1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"

r = s.lengthLongestPath(s1)
print r
