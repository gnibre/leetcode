# first attempt was wrong about one thing.
# if  pre > 1
# if  x can not be as big square as (pre+1)
#    x can possiblly be any size  that  sz <= pre+1
#    but i set x = 1  when it happends. which is wrong.
#  good so we can move hsum and wsum now.


# II
# read discuss.
# damn.
#  since  [h,w-1]  [h-1,w]  [h-1,w-1]  are ALL set when we are calculating [h,w]
#  [h,w] is just the min from above +1 and don't needed to do it one by one.

# it's moving hte suqare as a whole.
# my stupid hsum, wsum is kinda of similar idea, but use  row. col as whole.
# when have bigger vision,  square can be used directly.


class Solution(object):

    def maximalSquare(self, matrix):

        mh = len(matrix)
        if mh == 0:
            return 0
        mw = len(matrix[0])
        if mw == 0:
            return 0

        res = [[0 for x in range(mw + 1)] for y in range(mh + 1)]

        max_seen = 0
        for h in range(mh):
            for w in range(mw):
                if matrix[h][w] == '0':
                    continue
                res[h + 1][w + 1] = min(res[h][w + 1], res[h + 1][w], res[h][w]) + 1
                if res[h + 1][w + 1] > max_seen:
                    max_seen = res[h + 1][w + 1]
        return max_seen**2

    def maximalSquare_slow(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        #  it over all the possible  square :  O(m*n*n)
        # matrix [0,0] -> [h,w]
        # max(matrix[0,0,h,w]) = max(matrix[0,0,h-1,w], matrix[0,0,h,w-1], or biggest square from right bottom corner)

        # define ms(h,w) => max square that have right,bottom corner right at [h,w]
        # so ms(h,w) = ms(h-1,w-1)+ possiblly 1  or  ANY SIZE FROM 0 to ms(h-1,w-1)

        mn = []
        for line in matrix:
            nl = []
            for n in line:
                nl.append(int(n))
            mn.append(nl)

        mh = len(mn)
        if mh == 0:
            return 0
        mw = len(mn[0])
        if mw == 0:
            return 0

        res = [[0 for x in range(mw)] for y in range(mh)]
        max_seen = 0
        for h in range(mh):
            for w in range(mw):
                # ms(h,w) =  ms(h-1,w-1) +1 if
                if mn[h][w] == 0:
                    continue
                res[h][w] = 1
                if max_seen == 0:
                    max_seen = 1
                if h > 0 and w > 0:
                    # print " h, w ,  %d  %d " % (h, w)
                    pre = res[h - 1][w - 1]
                    # print " pre -> %d " % pre
                    if pre > 0:
                        # check from h[ n to w-1] that have length pre
                        # check from w[ m to h-1] that have length pre
                        # if both satisfied,  ret pre+1

                        ssize = 1  # square size
                        for ex in range(1, pre + 1):
                            # binary search even?
                            if mn[h][w - ex] + mn[h - ex][w] == 2:
                                ssize = ex + 1
                            else:
                                break

                        res[h][w] = ssize
                        if res[h][w] > max_seen:
                            max_seen = res[h][w]
                            # print " max_seen :   hw: %d,%d" % (h, w)
                            # print "l: %d " % max_seen
        # print res
        return max_seen**2

s = Solution()
matrix = ["10100", "10111", "11111", "10010"]
matrix = ["11", "11"]
matrix = ["0001", "1101", "1111", "0111", "0111"]
# 0001
# 1101
# 1111
# 0111
# 0111
print s.maximalSquare(matrix)
