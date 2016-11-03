class Solution(object):
    
    #  dumb, picking it consective array.
    # should pick any with order.
    def wiggleMaxLength_cons(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        # dp[p][1] 1:up        array end at p, end with up
        # dp[p][0] 0: down.  
        ln = len(nums)
        if ln<2:
            return ln

        dp = [[1,1]]*ln
        
        max_seen = 1
        for i in xrange(1,ln):
            if nums[i]>nums[i-1]:
                dp[i][1] = dp[i-1][0]+1
                if dp[i][1]> max_seen:
                    max_seen = dp[i][1]
            elif nums[i]<nums[i-1]:
                dp[i][0] = dp[i-1][1]+1
                if dp[i][0]>max_seen:
                    max_seen = dp[i][0]
            else:
                dp[i][0] = 1
                dp[i][1] = 1
        return max_seen
        
        
        # O(N) greedy
    def wiggleMaxLength(self,nums):
        ln = len(nums)
        if ln<2:
            return ln
        upc = 0
        dnc = 0
        upn = 1
        dnn = -1
        
        for i in xrange(ln-1):
            slope = nums[i+1]-nums[i]
            
            if slope*upn > 0:
                upc+=1
                upn*=-1
            if slope*dnn >0:
                dnc+=1
                dnn*=-1
            print "after %d " % nums[i]
            print "now,   up %d   down %d" % (upc,dnc)
        return max(upc,dnc)
        


s = Solution()
nums = [1,7,4,9,2,5]

r = s.wiggleMaxLength(nums)
print r        
        