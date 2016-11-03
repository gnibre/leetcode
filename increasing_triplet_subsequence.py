
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        #  k = 3 for now. 
        # what if k is 10 or 100
        
        
        # case k = 2
        # keep a smallest seen, anytime it get a bigger from stream, it works.
        
        # case k=3
        # keep a smallest seen?=>s, find another one. m that s<m , s->m
        # if any number came that have  v < m  , then  s->v
        # if any number came that actually e < s , then ?  s->v  and e 
        
        # stock trade?
        
        # stack of size 2;
        
        # put 
        
        if len(nums)<3:
            return False
        
        min_seen = nums[0]
        min_two_stack_s = ms = nums[0]
        min_twos_stack_m = mm = None
        
        for n in nums:
            if mm==None:
                if n>min_seen:
                    mm = n
                else:
                    min_seen = n
                continue
            
            if n<=min_seen:
                min_seen = n
            elif n>mm:
                # get
                return True
            else:
                #  min_seen < n < mm
                # 1  [min_seen, n] will be a new stack candidate
                # 2  [ms,mm] maybe updated to [ms,n]
                
                ms = min_seen
                mm = n
        any
            
        

s = Solution()
nums = [1]
nums = [1]
print s.increasingTriplet(nums)
