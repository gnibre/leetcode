import itertools

class Solution(object):

    def minPatches(self,nums,n):

        #  this problem is 'Hard' cause nums and n can be INF
        # should use generator, but not using  w = [0]*n to hold all

        #  greedy.

        #  if n is covered in sum(range(n))
        # til sum is all covered.

        covered = 0
        patch = []
        patch_count = 0
        s = 0

        max_covered = 0
        for x in nums:
            while x>max_covered+1 and max_covered<n:
                # patch.append(max_covered+1)
                patch_count+=1
                print "patching -> %d " % (max_covered+1)
                max_covered = max_covered*2+1
            # x can join now.
            print "x join => %d " % x
            max_covered = max_covered + x

            print " cur max: %d " % max_covered
            if max_covered>=n:
                break


        while max_covered<n:
            # patch.append(max_covered+1)
            patch_count+=1
            # print "patching -> %d " % (max_covered+1)
            max_covered = max_covered*2+1

        return patch_count






    def minPatches_SpaceN_failed(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        
        
        w = [0]*(n+1)
        ln = len(nums)

        for i in xrange(ln-1):
            # print "i => %d " % nums[i]

            w[nums[i]] = 1
            for j in xrange(i+1, ln):
                # print "j => %d " % nums[j]
                s = nums[i]+nums[j]
                if not s>n:
                    w[s] = 1

        w[nums[-1]]=1

        # print "w1 : %r " % w
        # sp = [sum(i) for i in itertools.product(w,repeat=1)] # generator? if nums too big.
        # product, cartecian is not what we needed.

        # for i in sp:
        #     w[i] = 1
        
        # print "w2 : %r " %w    
        
        patch =[]
        for i in xrange(1,n+1):
            if w[i] == 0:
                print " adding  %d " % i
                patch.append(i)
                for j in xrange(1, n-i+1):
                    if w[j]==1:
                        # print "wj %d => +pathch" % j
                        w[j+i] = 1  # patched with i
                        # print " %d => 1" % (j+i)
        
        return len(patch)



s = Solution()


nums = [1,3]
nums = [1,2,31,33]
# 4, 8, 16, 63
n = 2147483647
n = 120

nums = [1,2,2,6,34,38,41,44,47,47,56,59,62,73,77,83,87,89,94]
n = 20

r = s.minPatches(nums,n)
print r
