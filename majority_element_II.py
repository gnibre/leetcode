class Solution(object):
    def majorityElement(self, nums):
        
        if len(nums)<2:
            return nums
        slots = []
        
        
        for x in nums:
            print "do -> %d " % x
            i = len(slots)
            while i > 0:
                i-=1
                if slots[i][1]<1:
                    slots.pop(i)
                else:
                    slots[i][1] -=1

            inslots = False
            for i in xrange(len(slots)):
                if slots[i][0]==x:
                    slots[i][1]+=3
                    inslots = True
                    break
            if inslots:
                continue


            # x not in any
            # more slots available?
            if len(slots)<3: 
                print " adding to new slot."
                slots.append([x,2])

            # damage , -1 to all. already done.
        
            print "slots: %r " % slots

        ret = []
        for sl in slots:
            if nums.count(sl[0])>len(nums)/3:
                ret.append(sl[0])
        return ret
            
                
        
    
    def majorityElement_twoslotsfails(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if len(nums)<2:
            return nums
        
        n1 = n2 = None
        c1 = c2 = 0
        
        slots = []
        
        for x in nums:
            # get the tax running first.
            
            c1-=1
            c2-=1
            
            if c1>0 and n1==x:
                c1+=3
                continue
            if c2>0 and n2==x:
                c2+=3
                continue
            
            if c1<1:
                n1 = x
                c1 = 2 # set to 2 for over n/3
                continue
            if c2<1:
                n2 = x
                c2 = 2
                continue
            
            # x can not put it self in to n1 or n2, do something fun
        
        # n1 must be , n2 is not sure if it win the battle to stay with second place.
        # cause may only exist 1 element that >[n/3]
        
        # NO guarantee at all, return could be [] (not like I, always will have)
        rt = []
        if nums.count(n1)>len(nums)/3:
            rt.append(n1)
        if nums.count(n2)>len(nums)/3:
            rt.append(n2)
        
        
        return rt
            
                
s = Solution()
nums = [1,2]
nums = [1,2,3,4]

nums = [2,2]
nums = [1,1,1,3,3,2,2,2]
print nums
r = s.majorityElement(nums)
print r            