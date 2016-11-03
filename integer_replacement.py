class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # dp ? 
        # save +1 and -1 to later feels always more efficeint unless,  num+1 = 2^1000
    
        # 1024
        #       1022 1023 1024  512
        # 1021   1022 511  512
        
        # greedy? not got to 2^n  , maybe go to  2^n-1 , for case like  256*3, don't try to reach 1024 or 512, 
        
        # todo
        td = [n]
        dp = {}
        dp[1] = 0
        dp[3] = 2
        dp[5] = 3
        
        while len(td)>0:

            t = td.pop()
            print "----> %r " % t

            base,k = self.base(t)

            if base in dp :
                continue
            
            delay = False
            
            base_1, k1 = self.base(t-1)
            base_2, k2 = self.base(t+1)
            
            # print "b1: %d " % base_1
            # print "b1: %d " % base_2
            dl = []
            if base_1 not in dp:
                delay = True
                dl.append(base_1)
                # td.append(base_1)
            
            if base_2 not in dp:
                delay = True
                dl.append(base_2)
                # td.append(base_2)
            
            if not delay:
                dp[base] = min(dp[base_1]+k1,dp[base_2]+k2)+1
                print " get dp [%d ] => %d " % (base, dp[base])
            else:
                td.append(t) # add back, since it's not handled. will be handled after base_1 and base_2 are ready.

            td.extend(dl)

            # print "----> %r " % td
        
        base,k = self.base(n)

        print "final dp table : "
        for e in dp:
            print "[%d]=> %d " % (e,dp[e])

        
        return dp[base]+k
        
        
            
    
    def base(self,n):
        k = 0
        while n%2==0:
            n = n/2
            k+=1
        return n,k
        

    def integerReplacement_get_to_2_N_not_always_fastest(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # dp ? 
        # save +1 and -1 to later feels always more efficeint unless,  num+1 = 2^1000
    
        # 1024
        #       1022 1023 1024  512
        # 1021   1022 511  512
        
        # greedy?
        tt = 0
        
        
        while True:
            while n%2==0:
                n = n/2
                tt+=1
            if n==1:
                return tt
            print "/2/2-> %d " %n
            
            k = 2
            while k<n:
                k*=2
            
            hk = k/2
            # (k-n)-(n-hk)
            if k+hk>=2*n:
                # go to hk
                n-=1
                tt+=1
            else:
                # go to k
                n+=1
                tt+=1
            
            print "-> %d " %n
        return tt
        



s = Solution()


n = 100
n = 4
n = 65535
n = 111111111


r = s.integerReplacement(n)

print r