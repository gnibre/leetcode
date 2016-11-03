NBS = [[-1, 0], [1, 0], [0, 1], [0, -1]]


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        ret = []
        ht = len(matrix)
        if ht == 0:
            return ret
        wh = len(matrix[0])
        if wh == 0:
            return ret

    # 0, init,
    # 1, connected to Pa <- or ^
    # 2, connected to At  -> or _
    # 3, connected to both

        # init
        graph = [[0] * wh for x in xrange(ht)]

        visiting = []

        for w in xrange(wh):
            #  goes to Pa
            graph[0][w] |= 1
            visiting.append((0, w))
            #  goes to At
            graph[ht - 1][w] |= 2
            visiting.append((ht - 1, w))

        for h in xrange(ht):
            #  Pa
            graph[h][0] |= 1
            visiting.append((h, 0))
            #  At
            graph[h][wh - 1] |= 2
            visiting.append((h, wh - 1))

        ret.append([0, wh - 1])
        ret.append([ht - 1][0])

        while len(visiting) > 0:
            w, h = visiting.pop()
            for nb in NBS:
                w1 = w + nb[0]
                h1 = h + nb[1]
                if w1 > -1 and w1 < wh:
                    if h1 > -1 and h1 < ht:
                        # if graph[w1][h1]==0:
                        if matrix[w1][h1] >= matrix[w][h]:
                            # target is higher, so it will get my attribute

                            orig = graph[w1][h1]
                            graph[w1][h1] |= graph[w][h]
                            if orig != graph[w1][h1]:
                                # inlcude case graph[w1][h1] is just init (0)
                                visiting.append((w1, h1))

                                if graph[w1][h1] == 3:
                                    ret.append([w1, h1])

        return ret



s  = Solution()

matrix = 
r = s.pacificAtlantic(matrix)
