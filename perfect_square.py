import sys
import time

class Solution(object):
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FFailed this one.
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FFailed this one.
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FFailed this one.
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FFailed this one.
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FFailed this one.
    # Legendre's three-square theorem ; I get this right. n=x^{2}+y^{2}+z^{2}
    # but who hte fuck suppose to know fukcing  {\displaystyle n=4^{a}(8b+7)} n = 4^a(8b + 7) 
    # im not a fucking math doc
    # https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem


    def numSquares(self,n):
        
        sqrt = int(n**0.5)
        # case 1
        if sqrt*sqrt == n:
            return 1

        # coins = [i**2 for i in xrange(0, sqrt + 1)]


        # 1,4,9,16
        # 3  5  7
        coins = [0]*(sqrt+1)
        i = 1
        k = 1
        while i<sqrt+1:
            coins[i] = coins[i-1]+k
            k+=2
            i+=1

        #  case return 4:
        tmp = n
        while tmp%4==0:
            tmp /=4
        if tmp%8==7:
            return 4

        #  case return 2
        # half = n/2

        l = 1
        h = sqrt
        while l<=h:
            s = coins[l]+coins[h]
            if s > n:
                h -=1
            elif s<n:
                l+=1
            else:
                return 2

        # not 1,2,4, => 
        return 3

    # didn't give up yet.
    # 1, xrange instead of range
    # 2, order coins
    # 3, no more than 4 coins. ( conclusion from doing all case, don't know why)
    # 4, when pick coin a of value va, can not pick any coin that have value > ca
    def numSquares_welldone(self,n):
        # dp  = {}
        # sqrt = int(n**0.5)
        # coins = [i**2 for i in xrange(0, sqrt + 1)]
        # coins.reverse()

        dp = [0,1,2,3,1]+[sys.maxint]*n

        sqrt = 2
        nprd = 9
        for i in xrange(5,n+1):
            # coin pick
            # only pick one coin,  as the max pick. (greedy)
            # picked one coin c must satisfy:
            #  c^2 <=n
            # 4*c^2 >n  ( no more than 4 coins.)

            # make sure sqrt is still the sqrt of n
            if nprd==i:
                sqrt +=1
                nprd = (sqrt+1)**2
                dp[i] = 1
                continue
                # sqrprd = sqrt**2

            p = sqrt+1
            h = sqrt/2
            while p>h:
                p-=1
                prd = p**2
                if dp[i-prd]+1 < dp[i]:
                    dp[i] = dp[i-prd]+1
                    if dp[i] == 2:
                        break
                



            # for picked_coin in xrange(sqrt/2,sqrt+1):
            #     # print " working on %d ; sqrt %d  " % (i,picked_coin)
            #     prd = picked_coin**2
            #     if dp[i-prd]+1 < dp[i]:
            #         dp[i] = dp[i-prd]+1

            print "dp[%d] ====> %d  " % (i, dp[i])
        return dp[n]



    def numSquares_know_three_know_four(self, n):
        # cheat,
        # don't know hwy, but I get the conclusion from testing all
        # =>  res will always be 1 to 4, never get more than 4;
        # try use this as know theory.....

        # backward dp.

        sqrt = int(n**0.5)

        coins = [i**2 for i in range(1, sqrt + 1)]
        # coins.reverse()

        dp = [sys.maxint] * (n) + [0]
        idx = n + 1
        while idx > 0:
            idx -= 1
            # print " => idx  %d " % idx
            if dp[idx] > 3:
                continue
            for c in coins:
                if idx >= c:
                    dp[idx - c] = min(dp[idx - c], dp[idx] + 1)

                else:
                    break
        return dp[0]

    def numSquares_sad(self, n):
        """
        :type n: int
        :rtype: int
        """

        #  change of coin?
        sqrt = int(n**0.5)

        coins = [i**2 for i in range(1, sqrt + 1)]
        # coins.reverse()

        # print coins

        # dp = {}
        # dp[0] = 0
        # return self.dp(dp, coins, n)

        dp = [0] + [sys.maxint] * (n + 1)
        # res = [[]]*(n+2)
        # opn = 0

        for i in xrange(0, n):
            # if i==sys.maxint:
            #     # this num can't be matched by any coins. # will not happen actually, cause we have 1 in the coins.
            #     continue
            for c in coins:
                # opn+=1
                if i + c < n + 1:
                    dp[i + c] = min(dp[i + c], dp[i] + 1)
                    # if dp[i] + 1 < dp[i+c]:
                    #     dp[i+c] = dp[i] + 1
                    #     prel = list(res[i])
                    #     prel.append(c)
                    #     res[i+c] = prel
                else:
                    break


                    #  only happends when
                    # dp[i] is 1  or dp[i] is 2
                    #

            # dsqrt = int(i**0.5)
            # print "dp[%d] ====> %d  (%r)" % (i, dp[i],res[i])
            # if dsqrt**2 not in res[i] and (dsqrt-1)**2 not in res[i]:
            #     print "!!!!!!!!!!!! no a,a-1  %d " % dsqrt**2
            #     print "!!!!!!!!!!!! no a,a-1  %d " % (dsqrt-1)**2
            
        # print "total operations :  %d " % opn
        # print " r  :  %r " % (opn/n)

        return dp[n]

    def dp(self, dp, coins, n):
        if n in dp:
            return dp[n]

        l = [n - c for c in coins if n - c > -1]

        r = []
        # for i in l[:10]:
        for i in l:
            r.append(self.dp(dp, coins, i))

        dp[n] = min(r) + 1
        return dp[n]


s = Solution()

n = 9975
n = 88  # if take only 3;
n = 192  # wrong if only 5
n = 7168  # wrong if only 10
n = 200000
n = 23
n=5
st = time.time()
r = s.numSquares(n)

# n log n

et = time.time()
print r
print "time spent: %r " % (et-st)


# n = 100000
# st = time.time()
# i = -1
# while i<n-1:
#     i+=1
#     sqrt = int(n**0.5)
#     for j in xrange(0,sqrt):
#         sum = i+j
#         if i+j < 1000:
#             k = i if i>j else j
#         else:
#             k = j if j>i else i
# et = time.time()
# print "n log n time spent: %r " % (et-st)

# print r
