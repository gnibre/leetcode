class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        #  k=0,  just count
        #  k=len(s),  len(s)

        # dp? each interval have [s,e]
        # option is : pick, or not pick

        #  since , 26 chars, do 26 run of greedy alg

        #  'A'=>65  'Z'=>90

        chary = [[] for i in xrange(26)]  # 26 chars.

        cur = -1  # current expanding char index.
        curFrom = 0  # all char 'cur' from this position
        for idx in xrange(len(s)):
            ch = s[idx]
            chidx = ord(ch) - 65

            print " idx[%d] ch:  %s   chidx: %d " % (idx, ch, chidx)
            if chidx != cur:
                # end last char, switch to working on new char.
                print " new char."
                if cur > -1:
                    print " append to cur: %d " % cur
                    print "append  [%d, %d]" % (curFrom, idx - 1)

                    chary[cur].append((curFrom, idx - 1))
                    print chary[cur]
                cur = chidx
                curFrom = idx
            # else:
                # continue on last char. nothing to do

        print "====== final interval :"
        for chidx in xrange(len(chary)):
            ch = chr(65 + chidx)
            print " %s  :  %r " % (ch, chary[chidx])

        max_seen = 0
        for chidx in xrange(len(chary)):
            ch = chr(chidx + 65)
            # dp = {}
            ln = self.crw(chary[chidx], k)
            if ln > max_seen:
                max_seen = ln

        return max_seen


# characterReplacement with given ch
#  the first interval in the array, the length is already consumed,
#  improve, tree search, refound first interval on fail. like DFS
#  
    def crw(self, intervals, k):
        # (from,to) pairs
        # intervals = []
        ln = len(intervals)
        # only need to pick start interval, when it's picked. greedy.

        # state:  (current_length, k_left)

        # res = [(0, k)] * ln
        res = {}

        lastIntervalIdx = -1

        max_l = 0
        gap = 0
        for idx in xrange(ln):
            # for intervals started earlier,
            fr, to = intervals[idx]
            len_incr = to - fr + 1
            if lastIntervalIdx > -1:
                gap = fr - lastIntervalIdx - 1
            for sidex in res:
                cur_length, k_left = res[sidex]
                if k_left >= gap:
                    res[sidex] = (cur_length + k + len_incr, k_left - gap)
                else:
                    finish_length = cur_length + k  # add k chance of char change, make it k length longer.
                    max_l = finish_length if finish_length > max_l else max_l
                    del res[sidex]

            # for intervals start from here.
            # make this interval idx the first pick of intervals,

            res[idx] = (len_incr, k)

        #  return max_l.
        for idx in res:
            cur_len, k = res[idx]
            cur_len = cur_len + k
            max_l = cur_len if cur_len > max_l else max_l

        return max_l

    def gKey(self, l, k):
        return l * 20000 + k


s = Solution()
st = "ABCCCDEADDDFDKKJFFFFBBBBBBIIKDIDKDIAIAIDIDIDKAI"
st = "AAABBBBBCCCCCDDDDDEEEEEEEAAABBBBDDDDKKKKKAAABBB"
k = 3
print st
r = s.characterReplacement(st, k)
print r
