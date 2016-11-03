

#  from add operator
# it list all..

# here we shall d_n_q?

# Assume  b[x] is the last one bursted,
# when we are doing sub lists, we don't need to consider anything out side the list anymore
# it's a split, perfect, the scale get down to half, which means we are doing O(logn) steps to finish the whole thing, but not o(n!)

# the reason is that, after we made the assumption,  b[x] is hte last,
# so when we do b[x], we get 1*b[x]*1 coins,  cause it's last, no others left.
# which means don't need to consider how good sublist is doing, it doesn't matter already.


class Solution(object):

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.hit = 0
        self.miss = 0
        # return self.maxCoinsAux([1] + nums + [1])
        dp = {}
        r = self.maxCoinsDP(nums, dp, 0, len(nums) - 1, 1, 1)
        print "hit: %d " % self.hit
        print "miss: %d " % self.miss
        print "size:  %d " % len(dp)
        return r

    # def getKey(self, st, ed, lb, rb):
    #     return ','.join([str(st), str(ed), str(lb), str(rb)])

    def getKey(self, st, ed, lb, rb):
        return ((st*501+ed)*501+lb)*501+rb

    # use dp, so , record  offset [st,ed] from nums, also record left boundary, right boundary
    def maxCoinsDP(self, nums, dp, st, ed, lb, rb):
        if st>ed:
            # print "ohohoho"
            return 0

        if st == ed:
            return lb * nums[st] * rb

        max_coins = 0
        key = self.getKey(st, ed, lb, rb)
        if key in dp:
            # print " hit "
            self.hit += 1
            return dp[key]
        # print "miss"
        self.miss += 1

        for p in xrange(st, ed + 1):
            coins = self.maxCoinsDP(nums, dp, st, p - 1, lb, nums[p]) + \
                lb * nums[p] * rb + \
                self.maxCoinsDP(nums, dp, p + 1, ed, nums[p], rb)
            if coins > max_coins:
                max_coins = coins
        dp[key] = max_coins
        return max_coins


        # k(100) = 200*k(50) = 200*100*k(25)

    def maxCoinsAux(self, nums):

        ln = len(nums)
        if ln == 3:
            # two boundary, and one ballon,
            return reduce(lambda x, y: x * y, nums)

        # if st in dp and ed in dp[st]:
        #     return dp[st][ed]

        max_coins = 0
        for p in xrange(1, ln - 1):
            # assume p is the last pick in this list
            v = nums[p]
            coins = self.maxCoinsAux(nums[:p] + [v]) + nums[0] * v * nums[-1] + self.maxCoinsAux([v] + nums[p + 1:])
            if coins > max_coins:
                max_coins = coins

            if ln == 6:
                print "%r ;  pick %d, max : %d " % (nums, v, coins)
        return max_coins


s = Solution()


nums = [3, 1, 5, 8]
nums = [1,6,8,3,4,6,4,7,9,8,0,6,2,8]
nums = [42,23,62,2,89,97,26,82,47,23,9,2,9,11,53,49,40,3,88,76,63,11,79,37,52,91,5,44,71,69,20,5,74,41,70,68,26,16,62,53,47,46,26,27,99,72,4,40,77,74,89,19,26,7,30,79,49,75,51,28,47,26,55,81,82,15,21,89,51,10,0,50,31,32,38,7,99,13,23,98,68,9,54,15,34,52,58,48,66,75,6,15,91,33,15,37,25,98,98,77,60,16,82,89,48,43,1,85,39,99,95,86,45,90,73,45,93,99,39,57,32,47,35,79,25,54,98,34,60,90,38,40,5,5,96,21,18,93,69,38,85,49,15,77,84,70,52,87,73,15,65]
print len(nums)

import time

st = time.time()
r = s.maxCoins(nums)
ed = time.time()


print r

print " cost :  %r  " % (ed-st)