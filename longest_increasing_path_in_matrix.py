OFFS  = [ [0,1],[0,-1],[-1,0],[1,0] ]

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        
        # dp? cause longest from any point.
        
        # y, cuase it's increasing, we can just delete the value to replace it with seq-path, to do it inplace.
        
        rows = len(matrix)
        if rows==0:
            return 0
        cols = len(matrix[0])
        if cols == 0:
            return 0
            
        
        dp = [[0 for i in xrange(cols)] for j in xrange(rows)]
        
        pl = [] # list pending so we don't run into stackoverflow.
        mx= 0 #max seen so far.
        for r in xrange(rows):
            for c in xrange(cols):
                #print "[iter]"

                v = self.discover(dp,matrix,r,c,pl)

                #print " pl:  %r " % pl
                while len(pl)>0:
                    # handle pending list before go through.
                    vertex = pl.pop()
                    self.discover(dp,matrix,vertex[0],vertex[1],pl)
                #print " <- pl clear"
                for xx in xrange(len(dp)):
                    #print dp[xx]
                if v==0:
                    v = self.discover(dp,matrix,r,c,pl)

                if v>mx:
                    mx = v
                #print "===> %d %d => %d " % (r,c,v)
        return mx
    
    
    def discover(self,dp,matrix,r,c,pl):
        #print "discover--> %d,%d " % (r,c)
        if dp[r][c]>0:
            return dp[r][c]
        val = matrix[r][c]
        max_length = 0
        pending = []
        for off in OFFS:
            r1=r+off[0]
            c1=c+off[1]
            if r1>-1 and r1<len(matrix):
                if c1>-1 and c1<len(matrix[0]):
                    if matrix[r1][c1]>val:
                        if dp[r1][c1]>0:
                            if dp[r1][c1]>max_length:
                                max_length = dp[r1][c1]
                        else:
                            #print " adding [%d,%d]to pl" % (r1,c1)
                            pending.append([r1,c1])
                            break
        # 0 -> pending til pl list get finished running.
        if len(pending):
            #print "pending %d,%d :  %d " % (r,c, dp[r][c])
            pl.append([r,c])
            pl.extend(pending)
            return 0
        
        dp[r][c] = max_length+1
        #print "get--> %d,%d :  %d " % (r,c, dp[r][c])
        return dp[r][c]


s = Solution()
m = [[3,4,5],[3,2,6],[2,2,1]]

for i in xrange(len(m)):
    #print m[i]

r= s.longestIncreasingPath(m)
#print r
