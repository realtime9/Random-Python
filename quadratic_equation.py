import cmath 
a = float(input("Please enter the first number: "))
b = float(input("Please enter the second number: "))
c = float(input("Please enter the third number: "))
d = (b**2) - (4*a*c)
sol1 = (-b + cmath.sqrt(d)) / (2*a)
sol2 = (-b - cmath.sqrt(d)) / (2*a)
print(sol1)
print(sol2)

