class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #  numbers in the interval much easier? cause it's only one data structual of all time.
        #  similar , interval tree, once we find the filled spot, O(lgN) to update the tree? expected, only if the tree is balance.
        #  how about build the tree for the whole array. so count can be presented with binary search tree.
        #

        # doing 1 :

        # 00010001
        # 0123456789
        # 01 23 45 67 89 10
        # 0123 4567 89
        # 01234567  89

        print nums
        ln = len(nums)
        cache = {}

        # ln = 35  => 32 + 2 + 1
        # 100011  35
        #  idx [0 to 34]

        # init cache.
        base = 1

        while True:
            sz = (ln - 1) / base + 1
            cache[base] = [0] * sz
            if base >= ln:
                break
            base *= 2

        cap = base

        print " inited cached: %r " % cache
        nwp = [(nums[i], i) for i in xrange(ln)]
        # nwp = sorted(nwp, key=lambda t: ln * t[0] - t[1])
        nwp = sorted(nwp)

        print " get v with pos: %r " % nwp

        res = [0] * ln

        # cur = 0
        for v, p in nwp:
            c = self.getCount(cache, cap, 0, p - 1)
            res[p] = cache[cap][0] - c

            # print " pos: %d , v %d  , smaller number to the right : %d " % (p, v, res[p])
            self.record(cache, cap, p)

        return res

    def record(self, cache, cap, p):
        # print " record: p : %d " % p
        step = cap
        while step > 0:
            cache[step][p / step] += 1
            step /= 2
        # self.pc(cache)

        # print " query?  current number before p : %d  " % self.getCount(cache, cap, 0, p - 1)

    def pc(self, cache):
        for i in cache:
            print " %d  =====> %r " % (i, cache[i])

    #  num in cache,  from f to t,  include f and t
    #  also f must be devided by step, or equals to 0
    def getCount(self, cache, step, f, t):
        # print " get cound ; step %d;  f %d; t %d;" % (step, f, t)
        # f 0, t 7, step 8 ; perfect.   t>=8, need to invove next call
        #  t<8, current step too big, should use smaller
        if f > t:
            return 0
        if f == t:
            return cache[1][f]

        # if f + 1 == t:
        #     return cache[1][f] + cache[1][t]

        if f + step - 1 == t:
            return cache[step][f / step]

        if f + step - 1 < t:
            return cache[step][f / step] + self.getCount(cache, step / 2, f + step, t)
        else:
            # f+step-1>=t ;
            # step too big.
            return self.getCount(cache, step / 2, f, t)


s = Solution()

nums = [3, 5, 8, 1, 2, 7, 9, 1]
nums = [5, 2, 6, 1]

r = s.countSmaller(nums)

print r
