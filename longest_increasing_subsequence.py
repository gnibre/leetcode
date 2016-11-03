# subcase of terrible Russion Dolls...

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # number will be read once only, 
        # given number,  get performance  num-> p  ( if this number is tail of a subsequeence, what's the max length of it.)
        # if p overlap with other num that alredy there eailier,  say o_num => p
        # if num < o_num, then, replace it. 
        # if num >= o_num,  then ,discard it. 
        # if p is max ever, store it.
        
        
        res = []
        
        for n in nums:
            idx = len(res)
            p = 1
            # best position.
            while idx>0:
                idx-=1
                if res[idx][1]<n:
                    p = idx+1
                    break
            if p==len(res):
                res.append([p,n])
            else:
                # already have other number with same performance p;
                if n<res[p][1]:
                    res[p] = [p,n]
        
        return len(res)-1
                
        
        
        
        