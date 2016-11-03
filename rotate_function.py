
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        # math? diff F(i+1)-F(i)
        # 1 copy of everyting, and -(len-1) copy of last A[i]
        # so, if the choosen number is biggest, i thing that's the biggest number?
        
        # get F(0), and O(1) get F(i)
        
        
        # F(i+1) = F(i)+ (len-1)V_first -(sum_all-v_first)
        
        ms = f0 = self.f0(A)
        sm = sum(A)
        ln = len(A)
        cur = f0

        print " f0: %d " % f0
        for i in xrange(1,ln):
            #  i = 1,  
            fi = cur - A[ln-i]*ln + sm
            if fi>ms:
                ms = fi
            cur = fi
            print " f0: %d " % cur
        return ms
        
        
    def f0(self,A):
        l = [ i*A[i] for i in xrange(len(A))]
        return sum(l)




s = Solution()


nums = [4,3,2,6]
nums = [1,2,3,4,5,6,7,8,9,10]
r = s.maxRotateFunction(nums)


print r