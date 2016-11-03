# cannot use name Dstring.... why?

class DeString:
    def __init__(self,s):
        
        # c = s.count('[')
        # if c==0:
        #     s = s
        
        self.dstrList = self.decodeToList(s)

        print "destring created:  %r " %self.dstrList
    
    
    def decodeToList(self, s):
        res = []
        rem = s
        while len(rem)>0:
            spl = self.splitString(rem)
            res.append([spl[0],spl[1], spl[2]])
            rem = spl[3]
            print " token=> %r " % res
            print " rem=> %r " % rem
        return res
            
        #  get first token to num, decode string s1 that repeat num times; keep remain in s2
        # 3[a2[c]] => 3, a2[c] , '' 
        # 3[a]2[bc] => 3, a  , 2[bc]
    def splitString(self,s):

        if '[' not in s:
            return [s,0,'',[]]


        lpc = 0
        i = 0
        firstL = 0
        while i<len(s):
            if s[i]=='[':
                if firstL==0:
                    firstL = i
                lpc+=1
            if s[i]==']':
                lpc-=1
                if lpc==0:
                    break
            i+=1
        # n  = int(s[:firstL])

        extratoken = ''
        n=0
        tokenAndNum = s[:firstL]
        for x in xrange(firstL):
            if s[x]>='0' and s[x]<='9':
                extratoken=s[:x]
                n = int(s[x:firstL])
                break
        s1 = s[firstL+1:i]
        s2 = s[i+1:]
        # print "split:  s1%s + s2%s" % (s1,s2)
        return [extratoken,n,s1,s2]
    
    def decode(self):
        res = []
        for numedStr in self.dstrList:
            ch = numedStr[0]
            res.append(ch)
            repeat = numedStr[1]
            token = numedStr[2]
            print " ch %s followed by: %d => %s " % (ch, repeat,token)
            if '[' in token:
                ds = DeString(token)
                # ds = DString(token).decode()
                dcs = ds.decode()
                res.append(dcs*repeat)
            else:
                res.append(token*repeat)
        
        print "str: %r    de===>  %r  " % (self.dstrList, res)
        return ''.join(res)




class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        ds = DeString(s)

        return ds.decode()
            
        



s = Solution()
st= "3[a]2[bc]"
st = "3[a2[c]]"
st = "2[abc]3[cd]ef"
# ds = DeString(st)

print st
r = s.decodeString(st)
print r 