__author__ = 'super star'

def printTable(n,acity,bmatrix):
    print
    print '\t','\t','\t','\t','\t',
    for i in range(0, n):
        print "{:>15}".format(acity[i]), "\t",

    print
    for i in range(0, n):
        print "{:>15}".format(acity[i]), "\t",
        for j in range(0, n):
            print "{:>15}".format(bmatrix[i][j]), "\t",
        print