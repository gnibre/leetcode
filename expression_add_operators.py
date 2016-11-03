OPLIST = ['+', '-', '_', '*']



#  with node model A+B*C , dp failed.
# num of length 10 cost 3 seconds. 140k nodes created.
#  caues it's 4^n, even with l = 10 it's alot.

# devide and conquer?

#  12345 ? 6789

# +,-   good, subcase already
#  * not bad?
#  subcases cover?
#  123  45*6*7  89
#  _  similar to *


# cut operator :  + and -
#  good, subcase ready to go.

# connect operator:  _ and * 
# became pre? good, so all pre will have no + or - 




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




# state, A+B is enough, not A+-B*C
# the C is removed cause when we receive prestate, and cur remain num
#  the _ can not be between,  all the _ is handled alrady.

# dpsate, A, B, tail_num_list
class Solution(object):

    def addOperators(self,num,target):

        self.ret = []
        self.ct = 0

        ln = len(num)
        if ln==0:
            return self.ret

        self.addOperatorsAux("",0,0,num,target)


        print "total count: %d " % self.ct
        return self.ret


    # 2^n ;  
    def addOperatorsAux(self, pre, a, b, num, target):
        self.ct+=1

        # print "  (%d)+(%d) num:  %s " % (a,b,num)
        evl = a+b
        # print " cur evl: %d " % evl

        ln = len(num)

        if ln == 0:
            if evl == target:
                # print " ret : %s"%pre
                self.ret.append(pre)
            return

        h0 = num[0]

        til = ln+1
        if h0=='0':
            til = 2 # length most = 1

        for i in xrange(1,til):

            h = int( num[:i] )
            t = num[i:]

            if len(pre)==0:
                # init case.
                self.addOperatorsAux(num[:i],0,h,t, target)
            else:
                # +
                self.addOperatorsAux(pre+"+"+num[:i], evl, h, t,target)

                # -
                self.addOperatorsAux(pre+"-"+num[:i], evl, -h, t,target)

                # *
                self.addOperatorsAux(pre+"*"+num[:i], a, b*h, t, target)






s = Solution()
# num = [1, 2, 3]

import time

st = time.time()

num = "123"
target = 6

num = "3456237490"
target = 9191
target = 5

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
