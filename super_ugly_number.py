import heapq

#  heapq, is a heap or not?  why can't i use first n
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        #  k <=100; 
        # O(N) to get smallest
        
        
        # rule, list itself, became the base for each prime.
        k = len(primes)
        res = [1]
        pp = [0] * k  # prime list, next candidate index in the res.
        pc = [ [primes[i], i] for i in xrange(0,k)]
        hp = [] # used as heap to sort.
        for v in pc:
            heapq.heappush(hp,v)
        
        # mip = 0
        sz = 1
        
        while sz<n:
            mi = heapq.heappop(hp)
            cdd = mi[0]
            mip = mi[1]
            
            if res[-1] != cdd:
                res.append(cdd)
                sz+=1
            # even it's not added to res, pp should still be updated.
            pp[mip]+=1
            heapq.heappush(hp,[ res[pp[mip]]*primes[mip], mip])
        
        # print res
        return res[n-1]
        
        
        
        # while sz<n:
        #     # O(N)  # TLE at n =100,000
        #     mi = sys.maxint
        #     for i in xrange(0,k):
        #         cdd = res[pp[i]] * primes[i]
        #         if cdd < mi:
        #             mi = cdd
        #             mip = i
            
        #     # pick mip
        #     if res[-1] != mi:
        #         res.append(mi)
        #         sz+=1
        #     # even it's not added to res, pp should still be updated.
        #     pp[mip]+=1
        # print res
        # return res[n-1]
            