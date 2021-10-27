# #For a right angled triangle 
# b = int(input("Please enter the bredth of the trigangle: "))
# h = int(input("Please enter the height of the triangle: "))
# area = 0.5 * b * h
# print("The area of the trinagle is: ", area)

#For a non-right angled triangled 
#Using Heron's area of triangle formula

a = float(input("Please enter the value of the first side: "))
b = float(input("Please enter the value of the second side: "))
c = float(input("Please enter the value of the third side: "))

s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is: ", area)

