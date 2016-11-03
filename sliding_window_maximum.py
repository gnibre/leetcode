class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        if len(nums) < 1:
            return []
        
        #  when windown move ( dequeue ) , get next max from stack.
        maxQueue = []
        cur = k
        for i in xrange(k):
            self.addNum(maxQueue,nums[i],i)
            
        res = [maxQueue[0][0]]
        
        print maxQueue
        for i in xrange(0,len(nums)-k):
            self.removeNum(maxQueue,i+1)
            print maxQueue
            self.addNum(maxQueue,nums[i+k],i+k)
            print maxQueue
            res.append(maxQueue[0][0])
            
        
        # for i in xrange(len(nums)-k, len(nums)):
        #     self.removeNum(maxQueue,i)
        #     res.append(maxQueue[0][0])
        return res
    #  35812791
    #  87
    #  91
    
    #  mq : [v,idx]
    def addNum(self,mq,v,idx):
        # idx always bigger than previous 
        
        i = len(mq)-1
        while len(mq)>0 and v>mq[-1][0]:
            mq.pop()
        mq.append([v,idx])
    
    # idx is current window start; 
    def removeNum(self,mq,idx):
        while len(mq)>0 and idx>mq[0][1]:
            mq.pop(0)
    
    

s = Solution()

nums = [1,-1]
k = 1

print nums
r = s.maxSlidingWindow(nums, k)



print r