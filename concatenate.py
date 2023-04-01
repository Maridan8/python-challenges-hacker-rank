import numpy


N, M, P = map(int, input().split())

conc_array = numpy.array(input().split(), int).reshape(-1, P)
for _ in range(N + M - 1):
    curr_array = numpy.array(input().split(), int).reshape(-1, P)
    conc_array = numpy.concatenate((conc_array, curr_array))

print(conc_array)
