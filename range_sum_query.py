class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.zsum = []
        sm = 0
        for n in nums:
            sm += n
            self.zsum.append(sm)
        # print "==> %r " % self.zsum

        self.updated = {}

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """

        ori_val = self.zsum[i]
        if i > 0:
            ori_val -= self.zsum[i - 1]
        # print "orig:  %d " % ori_val
        diff = val - ori_val
        if diff == 0:
            if i in self.updated:
                del self.updated[i]
            return
        self.updated[i] = diff

        #  delay the value update,
        #  dont need update until the value is used.
        # or even, when only one value is updated, use the value.

    def apply_update(self):

        idx = 0
        diffsum = 0
        while idx < len(self.zsum):
            diffsum += self.updated[idx] if idx in self.updated else 0
            self.zsum[idx] += diffsum
            idx += 1
        self.updated = {}
        # print "apply after update %r " % self.zsum

    def sumRange(self, i, j):
        # print " sum rnage %d %d " % (i, j)
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """

        isupdated = False

        if len(self.updated) > 100:
            isupdated = True

        if isupdated:
            self.apply_update()

        offset = 0
        for k in self.updated:
            if i <= k and k <= j:
                offset += self.updated[k]
        if i == 0:
            return self.zsum[j] + offset
        return self.zsum[j] - self.zsum[i - 1] + offset


# Your NumArray object will be instantiated and called as such:

# nums = [1,3,5]

# numArray = NumArray(nums)
# print numArray.sumRange(0, 2)
# numArray.update(1, 2)
# print numArray.sumRange(0,2)


nums = [9, -8]
numArray = NumArray(nums)
numArray.update(0, 3)
print numArray.sumRange(1, 1)
print numArray.sumRange(0, 1)
print numArray.update(1, -3)
print numArray.sumRange(0, 1)

print "done"


# sumRange(0,2),update(1,2),sumRange(0,2)
