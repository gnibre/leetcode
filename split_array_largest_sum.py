
# minimize the largest sum; when spilit into m part.

#  non-negative numbers.


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """

        # m=1, well. is sum
        # m=n , well, is the max
        # max is the best case.
        #  minimal m to get max as the result of this problem:  don't know. best case : m=2
        #  say : [1,3,6, 999]
        #  when m>=minimal_m ; return max
        #  when m < minimal_m, result should be bigger than max,

        # if it's to verify given  max_sum, to verify if it's do able : O(n)   n=length of nums
        #  really? greedy works?
        #  range of max_sum  : from  max_of_list to sum_of_list

        #  if

        # this we have m, use dp, define the range of possible sum(max sum) to get it


        mx = max(nums)
        sm = sum(nums)


    #  return [f,t] if do able
    #  return None if not possible.
    def guessRange(self, dp, nums, sm, m, f, t):
        # sum range from [f,t] is it good for m picks

        #  for numbs, we got choice to stop at any time, for every choice that meet the critaria, redefine range.
        #  since picked numbers will possiblly affect lower bound [f], since the go is to find the minimual [f] that can devide the array of nums
        #  to m parts, that they all got sums <=f

        # it's going to be f(n) = f(n-1)+f(n-2)+.....+f(1) ; but since it's dp, worst case  it's n^3  (f*t*m)
        # unless we end it early.

        #  if no sum fit [f,t], when sum>t, it fails. and case ended earlier.
        #  if sum left > m* t ; fails early , when f is picked too low, goes to slow.

        #  when first interval is defined, we get [f,t] f=sum(interval), t = sum(interval+next)-1 
        #  cause after we split, we max_sum_in_each_interval will be t, other wise we can pick one more for first interval
        #  also, since f= fum(first_interval),  max_sum is >= f, so the range is [f,t]
        if m==1:
        	if sm>t:
        		return None
        	if sm>f:
        		return sm

        if len(nums)==0:


        pickedTil = -1












