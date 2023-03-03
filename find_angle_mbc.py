import math


AB = int(input())
BC = int(input())

# A median on the hypotenuse divides the right angled triangle in two
# isosceles triangles. MBC = MCB.
AC = math.sqrt(AB * AB + BC * BC)
theta = math.degrees(math.acos(BC / AC))

print(str(round(theta)) + "\N{DEGREE SIGN}")
