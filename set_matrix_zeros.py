class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        #  use extra space of up to  m+n with set.
        # can do that in palce,  with first row, and first col !!


        zrow = set()
        zcol = set()

        rows = len(matrix)
        if rows == 0:
            return
        cols = len(matrix[0])
        if cols == 0:
            return

        print "go"

        r = 0
        while r < rows:
            c = 0
            while c < cols:

                if matrix[r][c] == 0:
                    zrow.add(r)
                    zcol.add(c)
                c += 1
            r += 1

        print " get zrow and zcol:"
        print zrow
        print zcol

        for zr in zrow:
            c = 0
            while c < cols:
                matrix[zr][c] = 0
                c += 1
        for zc in zcol:
            r = 0
            while r < rows:
                matrix[r][zc] = 0
                r += 1


s = Solution()

matrix = [[0]]

s.setZeroes(matrix)
