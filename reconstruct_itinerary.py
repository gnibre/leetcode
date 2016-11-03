import collections

class Solution(object):
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            # print "a: %r " % a 
            # print "a: %r " % b
            # print "type : %r " % type(a)
            targets[a].append(b)
            
        route = []

        print targets

        
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]




s = Solution()


tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]



print tickets


r = s.findItinerary(tickets)


print r