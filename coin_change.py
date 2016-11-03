import sys
import time


##### another improvement that missed:

# only step on the points that can be reached!!  seems i did it? by testing with max.
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        print coins
        coins = list(set(coins))
        print coins
        dp = [0]+[sys.maxint]*(amount+1)  # amount => num_of_coins_needed. (-1 if not possible)
        # coins.reverse()
        
        idx = -1
        while idx<amount:
            idx+=1
            # from 0 to ammount
            if dp[idx]<sys.maxint:
                for c in coins:
                    if idx+c <= amount and (dp[idx]+1)<dp[idx+c]:
                        dp[idx+c] = dp[idx]+1
            else:
                print "-> skip  idx : %d " %idx

        # for a in range(1,amount+1):
        #     dp.append(self.canChange(dp,coins,a))
        #     # print "amount %d ->  %d " % (a,dp[-1])

        if dp[amount] == sys.maxint:
            return -1
        return dp[amount]
        
        
    def canChange(self,dp, coins,amount):
        minc = sys.maxint
        for c in coins:
            if amount>=c and dp[amount-c]>-1:
                minc = min(minc,dp[amount-c]+1)
        return -1 if minc==sys.maxint else minc



s = Solution()

coins = [253,27,214,340,158,92,52,126,466,431,95]
a = 3046
coins = [370,417,408,156,143,434,168,83,177,280,117]
a= 9953

st = time.time()
r = s.coinChange(coins,a)        
ed = time.time()

print r

print " cost : %r " % (ed-st)