class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        #  it's easier if median have no dupe, perfect devide and alter as you wish.
        #  if median count > len/2 , impossible
        #  if median count>1, do need to find a sort, and do it in place.
        #  so for cases median count > 1 
        #  what to do is alternate two lists,  or merge two sorted list(keep order)  
        
        # LM MG
        # MLMG
        # LLM MMG      LLMM WGG
        # MLL GMM      MMLL GGW
        # MGLMLM       MGMGLWL
        # ABCDE    abcd =>  AaBbCcDdE
        
        # ABCDE    dcba
        # AaCDE    dcbB
        
         
        # well, it's possible but too hard to do it inplace,  give up tring to do it inplace, but just merge it.
        # like ABCDE abcd =>  AaBbCcDdE , 
        
        
        # binary search find median? 
        
        #O(N) expected, but not always guarenteed, like quicksearch
        # inplace. 
        # median = medianSort(nums,0,len(nums)-1)
        
        #  ONLOG get median for now.
        # nums.sort()
        snums = sorted(nums)
        ln = len(nums)
        median = snums[ln/2]
        if ln%2==0:
            median = (snums[ln/2-1]+snums[ln/2])/2
        
        print "median:  %d " % median

        print nums

        # [L,M,G]  Less, median, Greater.
        # mc = nums.count(median)
        # if 2*mc>ln:
        #     not available.
        #     return False
        
        st = 0
        ed = ln-1
        write_st = 0
        
        while st<=ed:
            while nums[st]<median and st<=ed:
                nums[write_st] = nums[st]
                st+=1
                write_st+=1
            if st>ed:
                break
            if nums[st]==median:
                # throwaway.
                st+=1
            else:
                #  find nums[st]>median
                tmp = nums[ed]
                nums[ed] = nums[st]
                ed-=1
                nums[st] = tmp
            print nums
            print "st: %d  ed %d " % (st, ed)
        
        for i in xrange(write_st,ed+1):
            nums[i] = median
        

        print "sort with median"
        print nums


        #  sorted L_M_G now.
        ret = []
        gi = ln-1-ln/2
        
        for i in xrange(ln/2):
            ret.append(nums[ln-1-ln/2-i])
            ret.append(nums[ln-1-i])
            
        if ln%2==1:
            ret.append(nums[0])
        nums = ret
        
        return nums
    
    
    
    # some lib can do it in O(N)
    def findMedian(self, nums):
        # unsorted = [0,len(nums)-1]
        st = 0
        ed = len(nums)-1
        while st<ed:
            if ed==st+1:
                if nums[ed]<nums[st]:
                    t = nums[ed]
                    nums[ed] = nums[st]
                    nums[st] = t
                break
            
            mid = (nums[st]+nums[ed])/2
            bs = st
            be = ed
            cur = st
            
            
            

    #  only between st,ed are not sorted.
    #  *sort only to do:
    # 1 median in the mid,
    # 2 nums < median
    # def sortAndFindMedian(self, nums, st, ed):
    #     123345
    #     if ed<=st:
            
        
        
        
    
s = Solution();

nums = [1,2,3,2,2,2,3,1,1]
nums = [1,5,1,1,6,4]
nums = [1,1,2,1,2,2,1]
nums = [4,5,5,6]
nums = [4,5,5,6,6]
nums = [3,2,1,1,3,2]
print s.wiggleSort(nums)
    
        
        
        
    
    
    
    
    
    
    