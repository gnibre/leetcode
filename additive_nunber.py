class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # // first num,  can't be longer than (len(num)-1)/2    a*2+1 <=len(num)
        # //  second num, can't be longer than  (len(num)-len(n1))/2 
        # //  total cases, O(N^2)
        # // easy to verify?
        
        
        res = []
        
        for fe in xrange((len(num)-1)/2):
            for se in xrange(fe+1, fe+1+(len(num)-fe-1)/2):

                if self.isAdditiveNum(num, -1 , fe, se):
                    print " --> good start with"
                    print " -> %r " % num[:fe+1]
                    print " -> %r " % num[fe+1:se+1]
                    return True


                # n1 = list(num[0:fe+1])
                # n2 = list(num[fe+1:se+1])
                # # print "n1 : %r " % n1
                # # print "n2 : %r " % n2
                # nsum = self.bigIntAdd(n1,n2)
                # # print "nsum:  %r " % nsum
                # # print "compare %r " % num[se+1:]
                # match = True
                # for i in xrange(len(nsum)):
                #     if nsum[i]==int(num[se+1+i]):
                #         continue
                #     else:
                #         match = False
                #         break
                # if match:
                #     # se+1 to x with lenght len(nsum)
                #     res.append([fe,se,se+len(nsum)])
        
        # for v in res:
            # print "try : %r " % v
            # if self.isAdditiveNum(num, v[0],v[1],v[2]):
            #     return True
        return False

    def isAdditiveNum(self,num,fe,se,te):
        # filtered with first num and second num

        num1 = list(num[fe+1:se+1])
        num2 = list(num[se+1:te+1])
        if int(num1[0])==0 and len(num1)>1:
            return False
        if int(num2[0])==0 and len(num2)>1:
            return False
        print "znum1 %r " % num1
        print "znum2 %r " % num2
        print "znum2 %r " % int(num1[0])
        print "znum2 %r " % int(num2[0])

        #next number start from
        # print "go try:  %r " % num[:se]
        # print "   try:  %r " % num1
        # print "   try:  %r " % num2
        nnsf = te+1
        while True:
            print "n1 %r " % num1
            print "n2 %r " % num2
            n2c = list(num2)
            sumN = self.bigIntAdd(num1,num2)
            match = True
            # nextnumber start from [te+1, ]
            # length = len(sumN)
            # end at te+len(sumN)
            # end at should < len(num)
            # 

            if nnsf+len(sumN)-1>=len(num):
                return False
            print " sum %r " % sumN
            print "comming num: %r " % num[nnsf:]
            for i in xrange(len(sumN)):
                if sumN[i] == int(num[nnsf+i]):
                    continue
                else:
                    return False
            # match.
            num1 = n2c
            num2 = sumN
            nnsf += len(sumN)
            if nnsf==len(num):
                return True




    
    def bigIntAdd(self, n1, n2):
        res = []
        c = 0
        # n1 = list(n1)
        # n2 = list(n2)
        while len(n1)>0 and len(n2)>0:
            p1 = int(n1.pop())
            p2 = int(n2.pop())
            s = p1+p2+c
            res.append(s%10)
            c = s/10
            
        while len(n1)>0:
            p1 = int(n1.pop())
            s = p1+c
            res.append(s%10)
            c = s/10
        
        while len(n2)>0:
            p2 = int(n2.pop())
            s = p2+c
            res.append(s%10)
            c = s/10
        if c>0:
            res.append(c)
        

        res.reverse()
        return res
        
            

s  = Solution()
num = "11235813"
num = "12122436"
num = "199100199"
num = "19910011992"
num = "101"
r = s.isAdditiveNumber(num)
print "so?"
print r