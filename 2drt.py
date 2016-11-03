import sys

import heapq


SRD = [[-1, 0], [1, 0], [0, 1], [0, -1]]


class S():

    def rt(self, heights):
        rows = len(heights)
        if rows < 2:
            return 0
        cols = len(heights[0])
        if cols < 2:
            return 0

        self.rows = rows
        self.cols = cols

        # wall, is known grids that we know the final height of the water, and h
        # h,wh, r,c  ( height, water-height-will-leak-if-higher, row, col)

        # plan, get the wall from out side. make it bucket like.
        # pick shortest piece/grid. it will leak til it's surrounded by other walls that are higher

        # save final water height in whs
        whs = [[-1] * cols for i in xrange(rows)]

        # leak is from lowest wall, so when stopped, all touched grids are finalized
        # non-touched are these blocked by heigher walls that we can't reach.
        #  same height, continue, no ponding
        #  lower than cur, since we build wall from surrounding, lower will be ponding. and is also finalized.
        #

        wall = []
        for r in xrange(rows):
            for c in [0, cols - 1]:
                # v = (heights[h][w],h,w)
                heapq.heappush(wall, (heights[r][c], r, c))
                whs[r][c] = heights[r][c]

        for r in [0, rows - 1]:
            for c in xrange(1, cols - 1):
                heapq.heappush(wall, (heights[r][c], r, c))
                whs[r][c] = heights[r][c]

        #

        while len(wall) > 0:
            cw = heapq.heappop(wall)  # lowest piece.
            print " doing wall : %r " % (cw,)
            self.expand(heights, whs, wall, cw)

            # toExpand = self.expand(heights, whs, cw)
            # for ext in toExpand:
            #     self.expand(heights, whs, ext)

        # score
        sm = 0

        resss = [[-1] * cols for i in xrange(rows)]

        for r in xrange(rows):
            for c in xrange(cols):

                k = whs[r][c] - heights[r][c]
                # if k > 0:
                #     print ""
                resss[r][c] = k
                sm += whs[r][c] - heights[r][c]

        print " - go res. go "

        for r in heights:
            print r
        print " - go res. go. height. "

        for r in whs:
            print r

        print " res res res."
        for r in resss:
            print r

        return sm

    def expand(self, heights, whs, wall, cw):
        wh, r, c = cw
        toExpand = []
        #  neighbour * 4;
        for ofs in SRD:
            r1 = r + ofs[0]
            c1 = c + ofs[1]
            if r1 < 0 or r1 == self.rows:
                continue
            if c1 < 0 or c1 == self.cols:
                continue

            if whs[r1][c1] != -1:
                print " skip  visitied,  %d %d " % (r1, c1)
                continue

            if heights[r1][c1] > wh:
                # new wall.
                print " find new wall %r " % ((heights[r1][c1], r1, c1),)
                heapq.heappush(wall, (heights[r1][c1], r1, c1))
                whs[r1][c1] = heights[r1][c1]
            else:
                if whs[r1][c1] == -1:
                    print "set water level to %d " % wh
                    print " for :  %r " % ((heights[r1][c1], r1, c1),)
                    toExpand.append((wh, r1, c1))
                    whs[r1][c1] = wh

        for ext in toExpand:
            self.expand(heights, whs, wall, ext)

    def heapqplay(self, nums):
        print "play heapq"

        ls = nums

        print ls

        print "heapify"
        heapq.heapify(ls)
        print ls

        # ls.sort()

        k = sorted(ls)
        print ls
        print k

        print " start."
        while len(ls) > 0:
            heapq.heappush(ls, 88)
            print heapq.heappop(ls)
            print heapq.heappop(ls)


s = S()

buildings = [
    # [2, 9, 10],
    # [3, 7, 15],
    [5, 12, 13],
    [15, 20, 10],
    [19, 3, 8],
    [12, 30, 2]
]
# buildings = [[0, 5, 7], [5, 10, 7], [5, 10, 12], [10, 15, 7], [15, 20, 7], [15, 20, 12], [20, 25, 7]]
# nums = [58, 1, 34, 5, 7, 76, 989, 3221, 90, 90, 4353, 4]
# nums = [1, 2, 2, 6, 34, 38, 38, 38, 41, 44, 47, 47, 56, 59, 62, 73, 77, 83, 87, 89, 94, 99]
# ns = [5334, 6299, 4199, 9663, 8945, 3566, 9509, 3124, 6026, 6250, 7475, 5420, 9201, 9501, 38, 5897, 4411, 6638, 9845, 161, 9563, 8854, 3731, 5564, 5331, 4294, 3275, 1972, 1521, 2377, 3701]

r = s.rt(buildings)
print r

# s.heapqplay(nums)
