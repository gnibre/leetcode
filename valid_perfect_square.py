
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        a = 10
        b = num / 10

        while a != b:
            print " a %d ; b %d " % (a, b)
            if a == b + 1 or b == a + 1:
                return False
            a = (a + b) / 2
            b = num / a

        return a * a == num


s = Solution()


n = 5


ret = s.isPerfectSquare(n)

print ret
