class S():
    def hm(self, nums):
        # have mid
        # order, nlogn, reverse

        snums = sorted(nums, reverse=True)

        ln = len(nums)
        sm = sum(nums)

        dp = [{}] * ln

        print " sm: %d" % sm

        if sm % 2 == 1:
            return []

        k = sm / 2

        return self.listWithSum(dp, snums, k)

    def listWithSum(self, dp, nums, k):
        print " doing  k=%d  ;  %r " % (k, nums)
        if len(nums) == 0:
            return None
        key = len(nums) - 1
        if k in dp[key]:
            return dp[key][k]

        f = nums[0]
        if f > k:
            r = self.listWithSum(dp, nums[1:], k)
            dp[key][k] = r
            return r
        elif f == k:
            dp[key][k] = [f]
            return [f]
        else:
            # f<k
            tail = self.listWithSum(dp, nums[1:], k - f)
            if tail:
                dp[key][k] = [f] + tail
                return dp[key][k]

            tail2 = self.listWithSum(dp, nums[1:], k)
            if tail2:
                dp[key][k] = tail2
                return tail2


s = S()

# nums = [58, 1, 34, 5, 7, 76, 989, 3221, 90, 90, 4353, 4]
nums = [1, 2, 2, 6, 34, 38, 38, 38, 41, 44, 47, 47, 56, 59, 62, 73, 77, 83, 87, 89, 94, 99, 109]
# ns = [5334, 6299, 4199, 9663, 8945, 3566, 9509, 3124, 6026, 6250, 7475, 5420, 9201, 9501, 38, 5897, 4411, 6638, 9845, 161, 9563, 8854, 3731, 5564, 5331, 4294, 3275, 1972, 1521, 2377, 3701]

r = s.hm(nums)
print r
