import numpy


matrix = []

N = int(input())
for _ in range(N):
    matrix.append(numpy.array(input().split(), float))

print(round(numpy.linalg.det(matrix), 2))
