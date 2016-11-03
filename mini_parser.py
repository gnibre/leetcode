# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """


class NestedInteger(object):
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        self.il = []
        self.i = 0

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        self.il.append(elem)
        print "%r " % self.il
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        return self.il
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """

    def __str__(self):
        if self.i != 0:
            print "have int, i=> %d " % self.i
        return "have litst"


class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """

        #  for [, find the ] that pairs with it.
        #  for [] , correctly use ',' to split them, i wish  string.split(',') can be used. but. no .

        if len(s) == 0:
            return NestedInteger(0)

        if not s[0] == '[':
            return NestedInteger(int(s))

        #  is list.
        list_str = s[1:-1]
        list_elm = self.deserialize_list(list_str)
        return list_elm

    def deserialize_list(self, list_str):
        # split with ,
        element_str = []
        p = s = e = lp = 0
        while p < len(list_str):
            s = p
            if list_str[p] == '[':
                lp = 1
                p += 1
                # find pairing ]
                while p < len(list_str):
                    if list_str[p] == '[':
                        lp += 1
                    elif list_str[p] == ']':
                        lp -= 1
                        if lp == 0:
                            p += 1  # p move to , that after matching ]
                            element_str.append(list_str[s:p])
                            p += 1
                            break
                    p += 1

            else:
                # is interger.
                while p < len(list_str):
                    if list_str[p] == ',':
                        element_str.append(list_str[s:p])
                        p += 1
                        break
                    p += 1
                if p == len(list_str):  # last interger in the list, don't have matching , or ]
                    element_str.append(list_str[s:p])
        # get all elements in element_str

        listInteger = NestedInteger()
        # print " deserialize_list:  %s ;  items :   " % list_str
        # for elm_s in element_str:
        #     print "-> %s " % elm_s
        for elm_s in element_str:
            elm = self.deserialize(elm_s)
            listInteger.add(elm)

        return listInteger


s = Solution()
st = "[123,[456,[789]]]"
print st
ret = s.deserialize(st)
print ret
