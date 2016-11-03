from collections import Counter

class Solution(object):
    def minWindow_v_dumb(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        
        ln = len(t) # need
        
        req = Counter(t)
        chset = set()
        for ch in req:
            chset.add(ch)
            
        
        diff = ln
        cur = {}
        for ch in req:
            cur[ch]=0
        
        #  window, 
        # expand til it have req satisfied.
        # shrink, try to get a minimal window that still have req ( contain t) satisfied.
        # shrink: remove as many chars as possible when it still is satisfied.
        
        st = 0
        ed = -1
        
        for i in xrange(len(s)):
            ch = s[i]
            if ch in cur:
                cur[ch]+=1
                if not cur[ch]>req[ch]:
                    diff-=1
                    if diff==0:
                        ed = i
                        break
        

        
        if ed==-1:
            return ""
        

        mi = ed-st+1
        ms = st
        me = ed
        print " init %r " % s[ms:me+1]
        
        while True:
            while st <= ed and diff==0:
                if (ed-st+1) < mi:
                    mi = ed-st+1
                    ms = st
                    me = ed
                
                ch = s[st]
                if ch not in req:
                    st+=1
                    continue
                else:
                    cur[ch]-=1
                    if cur[ch]>=req[ch]:
                        st+=1
                        continue
                    else:
                        diff+=1
            print " not-s  : %r " % s[st:ed+1]
            #  get more in
            if ed==len(s)-1 and diff>0:
                break

            while diff>0 and ed<len(s)-1:
                ed+=1
                ch = s[ed]
                if ch not in req:
                    continue
                else:
                    cur[ch]+=1
                    if cur[ch]<req[ch]:
                        diff-=1
            
            print " s?  : %r " % s[st:ed+1]
                
        return s[ms:me+1]        
        
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """        
        
        req = Counter(t)
        cur = {}
        for ch in req:
            cur[ch]=0
        diff = len(t)
        
        
        st = 0
        ed = self.expand(s,-1,req,cur,diff)
        if ed==-1:
            return ""
        
        print " init get : %r " % s[st:ed+1]
        mi = ed-st
        ms = st
        me = ed
        while True:
            r = self.shrink(s,st,ed,req,cur)
            st = r[0]
            ed = r[1]
            if ed-st<mi:
                mi = ed-st
                ms = st
                me = ed
            print " shrink get cur best: %r " % s[st:ed+1]
            # expand
            ch = s[st]
            st+=1
            cur[ch]-=1
            ne = self.expandTilNext(s,ch,ed,cur)
            if ne==-1:
                break
            else:
                ed = ne

            print " expand get fit: %r " % s[st:ed+1]
        
        return s[ms:me+1]
            
            
    def expandTilNext(self,s,ch,ed,cur):
        p = ed+1
        while p<len(s):
            c = s[p]
            if c not in cur:
                p+=1
                continue

            cur[c] +=1
            if c == ch:
                return p
            p+=1
        
        return -1
    
    def expand(self,s,ed,req,cur,diff):
        ed+=1
        while diff >0 and ed<len(s):
            ch = s[ed]
            if ch in req:
                if cur[ch]<req[ch]:
                    diff -=1
                cur[ch]+=1
            if diff==0:
                return ed
            ed+=1

        return -1
            
    
    def shrink(self,s,st,ed,req,cur):
        while st<=ed:
            ch = s[st]
            if ch in req:
                if cur[ch]==req[ch]:
                    break
                else:
                    cur[ch]-=1
            st+=1
        return [st,ed]
            
            

        
sl = Solution()
s = "bdab"
t = "ab"

s = "a"
t = "aa"

s = "bba"
t = "ab"
r = sl.minWindow(s,t)        

print r