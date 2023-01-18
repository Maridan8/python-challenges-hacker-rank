import numpy


input_list = list(map(int, input().strip().split(" ")))

print(numpy.reshape(input_list, (3, 3)))
