import string
import time


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        # order by length?
        # order by non overlap?
        #

        # set1 set2.

        cm = {}
        for ch in string.ascii_letters:
            cm[ch] = set()

        ln = len(words)
        for i in xrange(ln):
            for ch in words[i]:
                cm[ch].add(i)

        # for ch in cm:
        #     if len(cm[ch])>0:
        #         print "%r =<%r "%(ch,cm[ch])

        return self.maxP(words, cm, range(ln), range(ln), ord('a'))

        # return maxP(words,words)

    # l1 l2, index of words
    # cm, set used to help compare.
    # ch, currently uncompared char ;  which means l1 and l2 will not have same char that smaller than ch.
    # when ch='k'  it's not possible that words from l1 and l2 both have 'a' or 'b' or 'c'
    def maxP(self, words, cm, l1, l2, ch):
        # print " %s ->   l1 : %r    l2 %r  " % (chr(ch), l1, l2)

        print " %s ->     " % chr(ch)
        print "l1 : %r  " % [words[i] for i in l1]
        print "l2 : %r  " % [words[i] for i in l2]

        if len(l1) == 0 or len(l2) == 0:
            return 0

        if ch > ord('z'):
            # end
            max1 = max2 = 0
            for i in l1:
                l = len(words[i])
                if l > max1:
                    max1 = l
            for i in l2:
                l = len(words[i])
                if l > max2:
                    max2 = l
            return max1 * max2

        cha = chr(ch)
        st = cm[cha]
        # next_ch = chr(ord(ch)+1)
        if len(st) == 0:
            return self.maxP(words, cm, l1, l2, ch + 1)

        w1 = [i for i in l1 if i in st]
        wo1 = [i for i in l1 if i not in st]
        w2 = [i for i in l2 if i in st]
        wo2 = [i for i in l2 if i not in st]

        # w1 wo2
        # wo1 wo2
        # wo1 w2
        return max([
            self.maxP(words, cm, w1, wo2, ch + 1),
            self.maxP(words, cm, wo1, w2, ch + 1),
            self.maxP(words, cm, wo1, wo2, ch + 1)
        ])

st = time.time()
s = Solution()
words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
r = s.maxProduct(words)
ed = time.time()
print r
print " time:  %r " % (ed - st)


# a abcw baz bar abcdef
# b abcw baz bar abcdef
# c abcw         abcdef
# d              abcdef
# e              abcdef
# f              abcdef   foo xtfn
# o                       foo
# r           bar
# t                             xtfn
# x                             xtfn
# n                             xtfn
# z      baz


# abcw baz bar abcdef  |  foo xtfn   ; posibility  every a map to every b

#  abcw baz bar , abcdeF  |  Foo, xtfn  ;  every aF map to non bNoneF

# filter f
#  abcw baz bar , abcdeF  |  Foo, xtfn
#  getting smaller set.

