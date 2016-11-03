class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        if rows==0:
            return False
        cols = len(matrix[0])
        if cols==0:
            return False
        
        
        return self.sm(matrix,target,0,0,rows-1,cols-1)
        
        
        #  if m[r][c] < target,  
        # if  m[bot][right] > target:     m[r+1][0] to m[bot][c]    m[0][c+1] to m[r][right] 
                                        #  m[r+1][c+1] to bot.right.
        
        # if m[r][c] > target 
        # if m[0][0] < target.
        #  m[0][0] to m[r][c]
        #   m[0][c] to m[r-1][right]
        #  m[r][0] to m[bot][c-1]
        
    
    def iterSearchMatrix(self, matrix, target, t, l , b, ri):
        for r in xrange(t,b+1):
            for c in xrange(l,ri+1):
                if matrix[r][c]==target:
                    return True
                if matrix[r][c]>target:
                    break
        return False
        
        
    def sm(self,matrix,target, t,l,b,ri):
        
        if t<0 or l<0:
            if b>=len(matrix) or ri>=len(matrix[0]):
                return False
        
        if t>b or l>ri:
            return False
        
        d = (t-b)*(ri-l)
        if d<100:
            return self.iterSearchMatrix(matrix,target,t,l,b,ri)
        
        
        if matrix[t][l] == target:
            return True
        elif matrix[t][l] > target:
            return False
        
        if matrix[b][ri] == target:
            return True
        elif matrix[b][ri] <target:
            return False
        
        r = (t+b)/2
        c = (l+ri)/2
        
        if m[r][c]==target:
            return True
        
        if m[r][c] < target:
            # right,down
            if self.sm(matrix,r,c,b,ri):  
                return True
            
        if m[r][c] > target:
            if self.sm(matrix,t,l,r,c):
                return True
        
        # other two square, will always check..
        # right. top 
        if self.sm(matrix,0,c+1,r,ri):
            return True
        # left, bot
        return self.sm(matrix,r+1,0,b,c-1)
        
    