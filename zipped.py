N, X = map(int, input().split())

marks = []
for _ in range(X):
    marks.append(map(float, input().split()))

# zip will get every value of each "column" in marks.
for student_marks in zip(*marks):
    print(sum(student_marks) / X)
