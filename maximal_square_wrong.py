# first attempt was wrong about one thing.
# if  pre > 1 
# if  x can not be as big square as (pre+1)
#    x can possiblly be any size  that  sz <= pre+1
#    but i set x = 1  when it happends. which is wrong.
#  good so we can move hsum and wsum now.




class Solution(object):




    def maximalSquare_wrong(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        #  it over all the possible  square :  O(m*n*n)
        # matrix [0,0] -> [h,w]
        # max(matrix[0,0,h,w]) = max(matrix[0,0,h-1,w], matrix[0,0,h,w-1], or biggest square from right bottom corner)

        # define ms(h,w) => max square that have right,bottom corner right at [h,w]
        # so ms(h,w) = ms(h-1,w-1)+ possiblly 1  or 0

        mn = []
        for line in matrix:
            nl = []
            for n in line:
                nl.append(int(n))
            mn.append(nl)
        matrix = mn

        mh = len(matrix)
        if mh == 0:
            return 0
        mw = len(matrix[0])
        if mw == 0:
            return 0

        hsum = []




        h = -1
        while h < mh - 1:
            h += 1
            hsum_h = [0]
            w = -1
            sm = 0
            while w < mw - 1:
                w += 1
                sm += matrix[h][w]
                hsum_h.append(sm)
            hsum.append(hsum_h)

        wsum = []
        w = -1
        while w < mw - 1:
            w += 1
            wsum_w = [0]
            h = -1
            sm = 0
            while h < mh - 1:
                h += 1
                sm += matrix[h][w]
                wsum_w.append(sm)
            wsum.append(wsum_w)

        res = [[0 for x in range(mw)] for y in range(mh)]

        print " final hsum  %r " % hsum
        print " final wsum  %r " % wsum

        max_seen = 0

        for h in range(mh):
            for w in range(mw):
                # ms(h,w) =  ms(h-1,w-1) +1 if
                if matrix[h][w] == 0:
                    continue
                res[h][w] = 1
                if max_seen== 0:
                    max_seen = 1
                if h > 0 and w > 0:
                    print " h, w ,  %d  %d " % (h,w)
                    pre = res[h - 1][w - 1]
                    print " pre -> %d " % pre
                    if pre > 0:
                        # check from h[ n to w-1] that have length pre
                        # check from w[ m to h-1] that have length pre
                        # if both satisfied,  ret pre+1

                        # w-1-n+1 == pre
                        # n = w-pre
                        # check h ,    n = w -pre , from n to w-1
                        #  use hsum(w) - hsum(n)
                        #  if n=0, use hsum(w-1)
                        hsum_res = hsum[h][w] - hsum[h][w - pre]
                        if hsum_res != pre:
                            continue

                        # check w sum,
                        #  w[ x to h-1] that have length pre.
                        #  h-x = pre  ;  x = h-pre
                        # from [h-pre to h-1]
                        wsum_res = wsum[w][h] - wsum[w][h - pre]
                        if wsum_res != pre:
                            continue

                        # damn, cool
                        res[h][w] = pre + 1
                        if res[h][w] > max_seen:
                            max_seen = res[h][w]
                            # print " max_seen :   hw: %d,%d" % (h, w)
                            # print "l: %d " % max_seen 
        print res
        return max_seen**2

s = Solution()
matrix = ["10100","10111","11111","10010"]
matrix = ["11","11"]
matrix = ["0001","1101","1111","0111","0111"]
# 0001
# 1101
# 1111
# 0111
# 0111
s.maximalSquare(matrix)