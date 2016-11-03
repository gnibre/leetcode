OPLIST = ['+', '-', '_', '*']


#  with keys set,  filter out different paths with same key path
# without keys set, TLE
#  without keys , cases: 340k for input length 10
# with keyset,  cases about 20 only for input legnth 10;

# since there're not many keys, store case for each key.


class OPNode():
    def __init__(self, a, pOrm, b, c, ix):
        self.a = a
        self.b = b
        self.c = c
        self.pOrM = pOrm  # 1 for plus, -1 for minus
        self.idx = ix
        self.nxt_v = None
        self.nxt_op = -1
        self.res = {}
        # self.eval_next_num()

    def eval_next_num(self, x):
        # case 1 ,  a,b, c*10+x
        # # case 2 ,  eval(a,b,c), +-1*x
        # # case 3   a+- eval(b*c) * x

        if len(self.res) > 0:
            return
        self.nxt_v = x
        # +
        v = self.evl()
        self.res[0] = OPNode(v, 1, 1, x,self.idx+1)
        #  -
        self.res[1] = OPNode(v, -1, 1, x,self.idx+1)
        #  _
        if self.c != 0:
            self.res[2] = OPNode(self.a, self.pOrM, self.b, int(self.c * 10 + x),self.idx+1)
        else:
            self.res[2] = None
        #  *
        self.res[3] = OPNode(self.a, self.pOrM, int(self.b * self.c), int(x),self.idx+1)
    def evl(self):
        return self.a + self.pOrM * self.b * self.c

    def get_op(self):
        return self.nxt_op

    def nxt_val(self):
        return self.nxt_v

    def has_nxt(self):
        return self.nxt_v is not None and self.nxt_op < 3

    def get_nxt(self):
        # self.eval_next_num()
        self.nxt_op += 1
        # return [self.res[self.nxt_op], OPLIST[self.nxt_op]]
        return self.res[self.nxt_op]

    def key(self):
        return "%d,%d,%d,%d,%d" % (self.a, self.b, self.c, self.pOrM, self.idx)

    def __str__(self):
        return "a: %r b: %r c: %r , nxt:  %r , op: %r " % (self.a, self.b, self.c, self.nxt_v, self.nxt_op)


class Solution(object):


    def addOperators(self,num,target):
        ln = len(num)

        dp = {}
        ct = 0

        if ln==0:
            return []

        initNode = OPNode(0, 1, 1, int(num[0]), 0)
        key = initNode.key()


        path = [initNode]

        keypath = []

        while len(path)>0:
            tNode = path[-1]
            plen = len(path)

            curkey = tNode.key()
            nxtVal = None


            if plen==ln:
                if tNode.evl() == target:
                    success_keys = [nd.key() for nd in path]
                    keypath.extend(success_keys)
            else:
                nxtVal = int(num[plen])
                tNode.eval_next_num(nxtVal) 

            if tNode.has_nxt():
                nnode = tNode.get_nxt()
                nkey = nnode.key()
                if nkey not in dp:
                    dp[nkey] = []
                    path.append(nnode)
                # else:
                #     print " dupkey : %s " % nkey
                # else case, will not add to path, dupe key.  this run is to get key.
            else:
                ct+=1
                path.pop()

        print keypath
        print dp

        print " total nodes:  %d " %ct
        print len(dp)



        return None











    #  no point with key to dedupe, since all the cases are wanted. and also we need to keep the path,
    #  so
    #  dfs.
    def addOperators_failss(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # dp? multiple?
        # ct = 0
        dup = 0
        ln = len(num)
        dp = {}  # key of cur sitiation to oplist. saved.
        if ln == 0:
            return []
        # if ln==1:
        #     if num[0]==target:
        #         return [str(num[0])]
        #     else:
        #         return []

        # idx
        initNode = OPNode(0, 1, 1, int(num[0]), 0)

        key = initNode.key()
        # print "init key : %r " % key
        

        fs = str(num[0])
        dp[key] = [""]
        path = [initNode]
        ops = []
        while len(path) > 0:
            # tailNode = path.pop()
            tailNode = path[-1]
            plen = len(path)
            # print " current tail node: %s " % tailNode
            curkey = tailNode.key()

            # if curkey not in dp:
                # print "fffffffffffffk curkey not in dp!!!  %r " % curkey

            nxtVal = None
            if len(path) == ln:
                if tailNode.evl() == target:
                    # ret
                    # print "match, ret from map:    %r " % dp[curkey]
                    ops.extend(dp[curkey])


                    # ret.append(self.getRet(fs, path))
            else:
                # print "len path? %d " % len(path)
                # print " -> nxt value possible:  %d " % num[len(path)]
                nxtVal = int(num[len(path)])

            if nxtVal is not None:
                tailNode.eval_next_num(nxtVal)

            if tailNode.has_nxt():
                nnode = tailNode.get_nxt()
                # print " -> putting next value to the queue  %s " % nnode
                if nnode is not None:
                    nxtkey = nnode.key()
                    if nxtkey not in dp:
                        dp[nxtkey] = []
                        # print " add node with key : %r  "  % nxtkey
                        path.append(nnode)

                    op = OPLIST[tailNode.get_op()]
                    # print " doing key: %r " % curkey
                    # print " doing ->  %r " % dp[curkey]
                    # print "doing with-> %r " % op
                    toExt = []
                    for pk in dp[curkey]:
                        # print " pk: %r " % pk
                        g = pk+op
                        # print g 
                        toExt.append(g)
                    # print " toext:   %r " % toExt
                    # toExt = [ ''.join([pk,op]) for pk in dp[curkey]]
                    dp[nxtkey].extend(toExt)

            else:
                path.pop()
                # ct += 1
        # print "total dupe processed: %d " % dup
        # print "total nodes processed: %d " % ct
        # print dp
        ret=  self.getRet2(num,ops)
        return ret

    def getRet2(self,nums,ops):

        def zipop(nums,op):
            ret = [nums[0]]
            for x in xrange(1,len(nums)):
                opc = op[x-1]
                if opc=='_':
                    opc = ''
                ret.append(opc)
                ret.append(nums[x])

            return ''.join(ret)

        return [zipop(nums,op) for op in ops]



    def getRet(self, f, path):
        ret = [f]
        for nd in path:
            if nd.nxt_val() is not None and nd.nxt_op > -1:
                if nd.nxt_op != 2:
                    ret.append(OPLIST[nd.nxt_op])
                ret.append(str(nd.nxt_val()))
        return ''.join(ret)

    def addOperators_bfs(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # dp? multiple?

        ln = len(num)
        if ln == 0:
            return []
        if ln == 1:
            if num[0] == target:
                return [str(num[0])]
            else:
                return []

        # A+-B*C
        # 3 => ABC
        #      0,3,0
        #      0,1,3

        # 35 => 0+-1*35
        #       0+-1*3+5
        # last digit 0:

        #  BFS,  every number, generates 3 kids, cld
        #  comming num:x ;
        # chld 1:  no op  c=> c*10+x
        # cld 2:  plus/minus   eval(pre)+- 1*x
        # child 3: multiplication  A+- eval(B*C)*x

        # init with ln>=2
        #  x1,x2
        # x1+-1*x2
        # x1x2
        # x1*x2

        # dp = {}
        # dp[a][b]

        dp = collections.defaultdict(dict)

        il = [
            [num[0], 1, num[1]],
            [0, 1, num[0] * 10 + num[1]],
            [0, 1, num[0] * num[1]]
        ]

        for l in il:
            self.save(dp, l)

        cur = il
        nxt = []
        for idx in xrange(2, ln):
            x = num[idx]
            for l in cur:

                a = l[0]
                b = l[1]
                c = l[2]
                # case 1 ,  a,b, c*10+x
                cld = []
                c1 = [a, b, c * 10 + x]
                # case 2 ,  eval(a,b,c), +-1*x
                c2 = [a + b * c, 1, x]
                c3 = [a - b * c, 1, x]
                # case 3   a+- eval(b*c) * x
                c4 = [a, b * c, x]

                cld = [c1, c2, c3, c4]

                for cl in cld:
                    if not self.isSeen(dp, cl):
                        nxt.append(cl)
            cur = nxt
            nxt = []

        # for cl in cur:

    def isSeen(self, dp, l):
        d = dp[l[0]]

        if l[1] not in d:
            d[l[1]] = set()
        seen = l[2] in d[l[1]]
        d[l[1]].add(l[2])
        return seen

    def key(self, a, b, c):
        return ','.join([str(x) for x in [a, b, c]])


s = Solution()
# num = [1, 2, 3]

import time

st = time.time()

num = "123"
target = 6

num = "3456237490"
target = 9191
# target = 5

r = s.addOperators(num, target)

ed = time.time()
print r

print " cost : %r " % (ed - st)


# st = time.time()
# for i in xrange(349525):
#     for j in xrange(10):
#         k = i * j
# ed = time.time()

# print " cost 2 :  %r " % (ed - st)
#  like each node , it have about 100 ooperations.
# for string  "3456237490" length about 10,  349525 total cases is too many.  4^10?
# back to bfs again?
