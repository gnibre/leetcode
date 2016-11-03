class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 0->1  6
        # 0->0  4
        # 1->1  7
        # 1->0  5
        offs = [[x, y] for x in range(-1, 2) for y in range(-1, 2)]
        offs.remove([0, 0])

        rows = len(board)
        if rows == 0:
            return
        cols = len(board[0])
        if cols == 0:
            return


        print "mask"
        #mask
        r = 0
        while r < rows:
            c = 0
            while c < cols:
                ct = 0
                for pair in offs:
                    r1 = r + pair[0]
                    c1 = c + pair[1]
                    if r1 > -1 and r1 < rows:
                        if c1 > -1 and c1 < cols:
                            ct += board[r1][c1] & 1
                print " looking at [%d][%d]=> %d ,  and ct: %d"%(r,c,board[r][c],ct)
                if board[r][c] == 1:
                    if ct < 2 or ct > 3:
                        #  1 => 0 ; 5
                        board[r][c] = 5
                    else:
                        board[r][c] = 7
                else:
                    if ct == 3:
                        # 0=>1  !!!
                        board[r][c] = 6
                    else:
                        # 0=>0
                        board[r][c] = 4
                c += 1
            r += 1

        print board

        print "off"
        # mask off
        r = 0
        while r < rows:
            c = 0
            while c < cols:
                board[r][c] = (board[r][c]&2)>>1
                c+=1
            r+=1


        print board




s = Solution()

board = [[1,1],[1,0]]

s.gameOfLife(board)