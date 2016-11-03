class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        if len(nums1) < 1 or len(nums2) < 1:
            return []

        maxv = nums1[-1] + nums2[-1]
        minv = nums1[0]+nums2[0]
        print "max : %d " % maxv

        if k > len(nums1) * len(nums2):
            l = self.smallestPairsLTV(nums1, nums2, maxv)
            l.sort(key=lambda p: (p[0] + p[1]))
            return l

        midv = (maxv- minv) * k / len(nums1) / len(nums2) + minv

        l = self.smallestPairsLTV(nums1, nums2, midv)
        while len(l) < k:
            print "max : %d " % maxv
            if midv == maxv - 1:
                midv = maxv
            else:
                midv = (midv + maxv) / 2
            l = self.smallestPairsLTV(nums1, nums2, midv)

        l.sort(key=lambda p: (p[0] + p[1]))
        return l[:k]

    def smallestPairsLTV(self, nums1, nums2, v):
        print "try smallestPairsLTV  with v : %d " % v
        ret = []
        for i in nums1:
            for j in nums2:
                if (i + j) <= v:
                    ret.append([i, j])
        return ret


s = Solution()

n1 = [0, 0, 0, 0, 0]
n2 = [-3, 22, 35, 56, 76]
k = 22
# n1 = [1, 1, 2]
# n2 = [1, 2, 3]
# k = 10

ret = s.kSmallestPairs(n1, n2, k)

print ret
