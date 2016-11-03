class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

#wrong, successor find by prime not in the list.

        if len(nums) < 2:
            return nums


        # cloud be like 1,2,10, 30, 60, 420, 840, 1680

        # dp,   ld(n) = max{ ld(n-i) +1 } ( any i < n)
        # worst case o(n^2)?  all prime,  all 1

        # seed set.

        # seeds = []  # tuples , order by  num?   compare with biggest num,  can not easily find value

        nums.sort()

        # sets = {}  # why sets is a map?  we  define sets use {bm=>nm} the biggest member in the set, and how many member is in the set.

        # we define  n_num : number_of_member_in_set_if_num_is_largest_element_in_set
        workshop = {}  # given num, put a mapping of num=>[n_num, bool_is_n_num bigger than another n_another when n>another]

        primes = self.getPrimeList(int(nums[-1]**0.5) + 1)
        plen = len(primes)

        hasone = False

        current_max_set_size = 0
        current_max_set_lead = 0
        for n in nums:
            if n == 1:
                hasone = True
                continue
            # print " ------->   working on %d " % n
            max_successor_size = 0
            successor_of_max = -1
            idx = -1

            # prime list cna only be used to help scan and find next successor..
            # successor have to be in the list,  still have to scan the nums list 


            # while idx < plen - 1:
            #     idx += 1
            #     p = primes[idx]
            #     if p * p > n:
            #         break
            #     if n % p == 0:
            #         dv = n / p
            #         if dv not in workshop:
            #             continue
            #         ws = workshop[dv]
            #         # n_n = ws[0]+1 # biggest set size if n is the max in the set.
            #         if ws[1]:  # biggest so far.
            #             max_successor_size = ws[0]
            #             successor_of_max = dv
            #             # if n_n>current_max_set_size:
            #             #     workshop[n] = [n_n, True]
            #             #     current_max_set_size = n_n
            #             # else:
            #             #     workshop[n] = [n_n, False]
            #             continue
            #         else:
            #             #  not biggest guaranteed.
            #             if ws[0] > max_successor_size:
            #                 max_successor_size = ws[0]
            #                 successor_of_max = dv

            n_max_size = max_successor_size + 1  # max size when n is biggest num in the set.
            if n_max_size >= current_max_set_size:
                current_max_set_size = n_max_size
                current_max_set_lead = n
                workshop[n] = [n_max_size, True, successor_of_max]
            else:
                workshop[n] = [n_max_size, False, successor_of_max]

            print " n %d  =>  %r " % (n, workshop[n])

        # get lead,
        res = []
        if hasone:
            res.append(1)

        n = current_max_set_lead
        while n > 0:
            res.append(n)
            n = workshop[n][2]

        return res

        # return current_max_set_size + 1 if hasone else current_max_set_size

    def getPrimeList(self, uplimit):
        workshop = [0] * (uplimit + 1)
        res = []
        #  from 2.
        idx = 2
        while idx < uplimit + 1:
            if workshop[idx] == 0:
                res.append(idx)
                j = idx * idx
                while j < uplimit + 1:
                    workshop[j] = 1
                    j += idx
            idx += 1
        return res


s = Solution()


nums = [1, 3, 5, 6, 99, 78, 92, 9]
nums = [1,2,4,8,9,72]
print nums
r = s.largestDivisibleSubset(nums)
print r
# pl = s.getPrimeList(10000)
# print pl
