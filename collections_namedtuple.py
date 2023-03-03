from collections import namedtuple


N = int(input())
student_tuple = namedtuple("student_tuple", " ".join(input().split()))

average_mark = 0.0
for i in range(N):
    average_mark += int(student_tuple(*input().split()).MARKS)
print(average_mark / N)
