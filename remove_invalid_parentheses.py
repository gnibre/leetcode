class Solution(object):


    #  removing one right parenthese is fast, close and easist way to get a valid result,
    # but it can also try to remove two parethese, if string after it gonna delete one more ')' anyway, it doesn't matter who delete that 
    # so, it seems more flexible than expected.
    # should have like least delete, choices of delete. to recover.
    # 1, one thing still sure:  have many parentheses are needed at least.


    def removeInvalidParentheses(self,s):

        sp = []
        
        ln = len(s)
        if ln == 0:
            return [""]


        lps = 0
        idx = st = 0
        # extraR=False
        while idx < ln:
            if s[idx] == '(':
                lps+=1
            elif s[idx]==')':
                lps-=1
                if lps<0:
                    # reset. 
                    seg = s[st:idx+1]
                    sp.append(seg)
                    st = idx+1
                    lps = 0
            idx+=1
        
        lastseg= s[st:]

        print " sp: %r " % sp
        print " last seg: %r " % lastseg

        lastseg_choices = [lastseg]
        if lps>0:
            rlastseg = self.reverseWithP(lastseg)

            print " last set running it agian ;   %r " % rlastseg
            lastseg_choices_reversed = self.removeInvalidParentheses(rlastseg)
            lastseg_choices = [self.reverseWithP(c) for c in lastseg_choices_reversed]




        # so far the same as my first approach.
        # for removing the extra ')', don't try to remove one ')' from each sp, instead,  for each comming sp part, randomly pick one ) from anywhere.
        # including it self ofc

        ret = ['']
        for sg in sp:
            w = [ r+sg for r in ret]
            print " w : %r "  % w
            ret = self.delRandomRP(w)
            print " ret : %r "  % ret



        # ret product with lastseg.
        print " ret prod with ls; ret :  %r " % ret
        print " ret prod with ls; lseg:  %r " % lastseg_choices
        nxt = []
        for r in ret:
            for ls in lastseg_choices:
                nxt.append(r+ls)

        print " final %r " % nxt
        return nxt



            
    #  def reverseWithP(self,s):
    
    def delRandomRP(self, w):
        ret = set()
        for s in w:
            for i in xrange(len(s)):
                if s[i]==')':
                    ret.add(s[:i]+s[i+1:])
        return ret

    def possibleStrWithExtraR(self, s):
        
        return ret




    def removeInvalidParentheses_WRONG(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        # remove.
        #  hwen it's valid? 
        #  stack. of how many ( already seen,  same num of )s gonna match 
        #  
        #  when ever extra ), must chose to remove one of them?  yes. otherwise can't match. nice.
        
        #  we get list of res[] now.  what to do is to merge.
        #  cartesian product of lists. 
        
        
        #  if can't be fixed. return [""]?? no keep removing......
        
        
        
        # after handle all the extra right parenthese cases,  the cases for  extra left parenthese that at the end of the string.  can be done by reverse, and do the same removeInvalidParentheses call again...
        #  but don't forget to reverse it back again... sucked.
        
        
        # after all these, got work on cartesian product
        
        sp = []
        
        ln = len(s)
        if ln == 0:
            return [""]
        
        lps = 0
        idx = st = 0
        # extraR=False
        while idx < ln:
            if s[idx] == '(':
                lps+=1
            elif s[idx]==')':
                lps-=1
                if lps<0:
                    # reset. 
                    seg = s[st:idx+1]
                    sp.append(seg)
                    st = idx+1
                    lps = 0
            idx+=1
        
        lastseg= s[st:]

        print " sp: %r " % sp
        print " last seg: %r " % lastseg

        #  hope it don't have extra '('s


        ret = set()
        sb = ''
        multiple_choices = [self.possibleStrWithExtraR(sg) for sg in sp]
        
        
        if lps>0:
            rlastseg = self.reverseWithP(lastseg)

            print " last set running it agian ;   %r " % rlastseg
            lastseg_choices_reversed = self.removeInvalidParentheses(rlastseg)
            lastseg_choices = [self.reverseWithP(c) for c in lastseg_choices_reversed]

            multiple_choices.append(lastseg_choices)

        else:
            multiple_choices.append([lastseg])
        
        # last seg will not have extra ), but may have extra left (
        
        
        ret = ['']
        for i in xrange(len(multiple_choices)):
            choices =   multiple_choices[i]
            if len(choices)==0:
                continue
            nxt = set()
            for pref in ret:
                for c in choices:
                    nxt.add(pref+c)
            ret = nxt
        
        return list(ret)
            
    def reverseWithP(self,s):
        r = s[::-1]
        rr = []
        for ch in r :
            if ch=='(':
                rr.append(')')
            elif ch==')':
                rr.append('(')
            else:
                rr.append(ch)
        
        return ''.join(rr)
        
        
    def possibleStrWithExtraR(self, s):
        ret = [ s[:i]+s[i+1:] for i in xrange(len(s)) if s[i]==')']
        return ret
        # for i in xrange(len(s)):
        #     if s[i]==')':
        #         r = s[:i]+s[i+1:]
        #         ret.append(r)
        
        
        
    
    
    #  when one more ) find ,  s is immediately handled here.
    def removeOneExtraRightParenthese(self,s):
        ll = len(s)-2 # last left p
        while ll > -1:
            if s[ll]=='(':
                # 
                break
        
        rp = [i for i in xrange(0,len(s)) if s[i]== ')' ]
        
        #  case ()()))))))) have 10 consective ) at end, ok to delete anyone.
        while len(rp)>1:
            if rp[-1] == rp[-2]+1:
                rp.pop()
            else:
                break
        
        # delete
        res = []
        for i in rp:
            fixedStr = s[:i]+s[i+1:]
            res.append(fixedStr)
        
        return res
        

s = Solution()
st = "()())()"
st = "(a)())()"
st = "()())()"
st = ")("
st = "(r(()()("
# st = "()())r)"
print " input:   %r " % st
r = s.removeInvalidParentheses(st)        
print r