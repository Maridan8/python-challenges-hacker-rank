import numpy


N, _ = map(int, input().split())
array = numpy.array([input().split() for _ in range(N)], int)

print(numpy.transpose(array))
print(array.flatten())
