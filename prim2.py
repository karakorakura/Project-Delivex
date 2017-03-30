__author__ = 'super star'


def prim1(n, Z, cities,totalcost):
    # z1=[n][n]



    visited = [0 for y in range(n)]
    min = 99999
    u = 0
    v = 0
    total = 0
    for i in range(0, n):
        visited[i] = 0
        for j in range(0, n):
            if Z[i][j] == 0:
                Z[i][j] = 0

    visited[0] = 1
    for count in range(0, n - 1):
        min = 99999
        for i in range(0, n):
            if visited[i] == 1:
                for j in range(0, n):
                    if i != j:
                        if visited[j] == 0:
                            if min > Z[i][j]:
                                min = Z[i][j]
                                u = i
                                v = j

        visited[v] = 1
        total = total + min
        Z[u][v] = Z[v][u] = 99999
        print "edge connect", u, " >>> ", v, '\t', cities[v], " to ", cities[u]
    totalcost[0]=total
    print total
    return Z
