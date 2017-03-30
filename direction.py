__author__ = 'super star'

import googlemaps
gmaps = googlemaps.Client(key='AIzaSyDECnwG-3AfclgdjEP3U57GA5bPWKe-LOc')
#dist = gmaps.directions('mumbai', 'delhi',mode='transit')
dist = gmaps.distance_matrix('amritsar', 'delhi')
#print dist

hours = dist[u'rows'][0][u'elements'][0][u'duration'][u'value']/3600.0
#print '{0:.1f}'.format(hours)

def timeFunction(source,destination):
    dist = gmaps.distance_matrix(source,destination)
    #print dist

    hours = dist[u'rows'][0][u'elements'][0][u'duration'][u'value']/3600.0
    #print '{0:.1f}'.format(hours)
    return hours

