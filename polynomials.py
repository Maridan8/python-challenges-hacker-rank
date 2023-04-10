import numpy


P = numpy.array(input().split(), float)
x = int(input())

print(numpy.polyval(P, x))
