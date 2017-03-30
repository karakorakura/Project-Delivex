from direction import timeFunction
from tabular import printTable

__author__ = 'super star'
from importlib import import_module
import prim
import prim2
import pandas
import copy

modulename = "prim"
import_module(modulename)
import_module("prim2")
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyDECnwG-3AfclgdjEP3U57GA5bPWKe-LOc')
dist = gmaps.distance_matrix('amritsar', 'delhi')


def mapdist(s, y):
    dist1 = gmaps.distance_matrix(s, y)
    y1 = dist1[u'rows'][0][u'elements'][0][u'distance'][u'value']
    return y1 / 1000


# print dist
row = dist[u'rows']
# print row
ele = row[0]
x = ele[u'elements'][0][u'distance'][u'value']
# print x/1000

no = int(raw_input('Enter number of different cities : '))
# print no
#################################################################################################
cities = []
k = 0

while len(cities) < no:
    if k == 0:
        cx = raw_input(' enter destination ')
    else:
        cx = raw_input(' enter city for seller ')
    k += 1
    cities.append(cx)



    # print cities
# print "this is cities";print cities[1]
matrix = [[0 for x in range(no)] for y in range(no)]

print
for i in range(0, no):
    for j in range(i, no):
        if i <> j:
            matrix[i][j] = mapdist(cities[i], cities[j])
            matrix[j][i] = matrix[i][j]

        else:
            matrix[i][i] = 0
    #progress
    progress =(i*j*100)/(no*no)
    print "## {}% ".format(progress),

print "## 100 % complete retrival"
print
########    matrix1 original

matrix1 = [[0 for x in range(no)] for y in range(no)]
matrix1 = copy.deepcopy(matrix)

print
printTable(no, cities, matrix)
print
##########       operation call
totalCost = [0]
matrix2 = [[0 for w in range(no)] for a in range(no)]
matrix2 = prim2.prim1(no, matrix, cities, totalCost)

printTable(no, cities, matrix2)

##########       matrix3 minimal spanning matrix

matrix3 = [[0 for w in range(no)] for a in range(no)]

for i in range(0, no):
    for j in range(0, no):
        matrix3[i][j] = 0
        if matrix2[i][j] >= 99998:
            matrix3[i][j] = matrix1[i][j]

print
print "\t \t \t Minimal spanning matrix final "
print

printTable(no, cities, matrix3)
print

print "\t \t \t Total cost proportional to {} units".format(totalCost[0])

###########         dfs and Stack

visited = [0 for w in range(no)]
stack = [[0 for j in range(2)] for w in range(no - 1)]

# stack[i][0] from stack[i][1] to

top = -1


def push(source, dest):
    global top
    top += 1
    stack[top][0] = source
    stack[top][1] = dest
    # print stack[top][0]," to ",stack[top][1]," ",top


def pop():
    global top
    top1 = top
    # print top
    top -= 1
    return stack[top1]


for i in range(0, no):
    visited[i] = 0


def dfs(n, graph, node):
    visited[node] = 1

    for i in range(0, n):
        if graph[node][i] != 0 and visited[i] == 0:
            push(i, node)
            dfs(n, graph, i)


dfs(no, matrix3, 0)

# time calculation
time = [0 for i in range(no)]
i = 0
temp1 = pop()
time[0] = timeFunction(cities[temp1[0]], cities[temp1[1]])

# Final routes
print
print "\t\t\t\t Final Routes "

print
print "go from ", cities[temp1[0]], " >>>> ", cities[temp1[1]], " in aprrox ", time[0], " hours "
print

while (top >= 0):
    if temp1[1] == 0:
        i += 1

        print " note: waiting time for each station may be included later approx(5 to 8 hrs)depending upon service conditions "
        print "...."
        print "total Route time (approx) {0:.1f} hours".format(time[i - 1] + 9)

    temp2 = pop()
    tempTime = timeFunction(cities[temp2[0]], cities[temp2[1]])
    if temp2[1] == temp1[1]:
        time[i] = max(tempTime, time[i])
    else:
        time[i] += tempTime
    temp1 = temp2
    print "go from ", cities[temp1[0]], " >>>> ", cities[temp1[1]], " in aprrox {0:.1f} ".format(tempTime), " hours "
    # print " note: waiting time for each station may be included later approx(5 to 8 hrs)depending upon service conditions "
    time[i] += 8

print
print " note: waiting time for each station may be included later approx(5 to 8 hrs)depending upon service conditions "
print "total Route time (approx) {0:.1f} hours".format(time[i - 1] + 9)
print



maxtime = 0

for i in range(0, no):
    if time[i] > maxtime:
        maxtime = time[i]
print
print " your items will be delivered in {0:.0f} ".format((maxtime / 24) + 1),"to {0:.0f} ".format((maxtime / 24) + 3),"days "
