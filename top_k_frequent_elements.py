import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # extra space allowed?    worst case,  O(N) space.

        cm = {}

        for n in nums:
            if n not in cm:
                cm[n] = 1
            else:
                cm[n] += 1

        print cm

        h = []
        for n in cm:
            heapq.heappush(h, [-cm[n], n])

        print h

        sml = heapq.nsmallest(k, h)

        print sml
        return [t[1] for t in sml]


s = Solution()

nums = [1,1,1,2,2,3]
k = 2


r = s.topKFrequent(nums,k)

print r