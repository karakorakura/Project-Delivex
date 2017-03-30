__author__ = 'super star'

import googlemaps
gmaps = googlemaps.Client(key='AIzaSyDECnwG-3AfclgdjEP3U57GA5bPWKe-LOc')
dist = gmaps.distance_matrix('amritsar', 'delhi')

def mapdist(s,y):
    dist1 = gmaps.distance_matrix(s, y)
    y1 = dist1[u'rows'][0][u'elements'][0][u'distance'][u'value']
    return y1/1000

#print dist
row = dist[u'rows']
#print row
ele = row[0]
x = ele[u'elements'][0][u'distance'][u'value']
#print x/1000

no = int(raw_input('Enter number of different cities : '))
#print no

cities = []

while len(cities)<no:
    cx = raw_input('enter ')
    cities.append(cx)
    #print cities
#print "this is cities";print cities[1]
matrix = [[0 for x in range(no)] for y in range(no)]

for i in range(0,no):
    for j in range(i,no):
        if i <> j :
            matrix[i][j]=mapdist(cities[i],cities[j])
            matrix[j][i]=matrix[i][j]
        else:
            matrix[i][i]=0

print '\t',
for i in range(0,no):
    print cities[i],"\t",

print
for i in range(0,no):
    print cities[i],"\t",
    for j in range(0,no):
        print matrix[i][j],"\t",
    print

