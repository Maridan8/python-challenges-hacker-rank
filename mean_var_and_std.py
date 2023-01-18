import numpy


n, m = map(int, (input().split()))

input_array = numpy.zeros((n, m))

for i in range(n):
    input_array[i] = list(map(int, (input().split())))

print(numpy.mean(input_array, axis=1))
print(numpy.var(input_array, axis=0))
print(numpy.std(input_array).round(11))
