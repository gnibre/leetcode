class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """

        rows = len(matrix)
        if rows == 0:
            return
        cols = len(matrix[0])

        # for each row, add [0] at the beginning.
        self.zsum = [([0] * (cols + 1)) for r in xrange(rows + 1)]

        for r in xrange(rows):
            for c in xrange(cols):
                # print matrix[r][c]
                self.zsum[r + 1][c + 1] = (self.zsum[r][c + 1] - self.zsum[r][c]) + self.zsum[r + 1][c] + matrix[r][c]   # row*col-1
                # print "->"
                # print self.zsum[r + 1][c + 1]

        # add 1 row and 1 col, life is so eazy.
        print " m:  "
        for x in xrange(len(matrix)):
            print matrix[x]

        print " created :  "
        for x in xrange(len(self.zsum)):
            print self.zsum[x]

        # print " created : %r " % self.zsum

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.zsum is None:
            return 0 
        print "r -> %d" % self.zsum[row2 + 1][col2 + 1]
        print "l -> %d" % self.zsum[row1][col1]

        print "f -> %d" % self.zsum[row1][col2]
        print "f -> %d" % self.zsum[row2][col1]

        r = self.zsum[row2 + 1][col2 + 1] + self.zsum[row1][col1] - self.zsum[row2+1][col1] - self.zsum[row1][col2+1]
        return r


matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]


# Your NumMatrix object will be instantiated and called as such:
numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)

print numMatrix.sumRegion(2,1,4,3)
# ,sumRegion(1,1,2,2),sumRegion(1,2,2,4)
