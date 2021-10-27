print("Hello World")
print("I love data science")
if 5 < 2:
    print ("5 is greater")
else:
    print("2 is greater")

x = "Ansh"
print(type(x))
x, y, z = "Ansh", "Ayush", "brothers"
print(x,y,z)
a = b = c = "Apples"
print(c)

names = ["Ron", "Harry", "Hermione"]
x, y, z = names
print(z)

z = 1j
print(type(z))

The random package
import random
print(random.randrange(1, 1000))

a = "Hello World"
print(a[3])
for x in "Ansh":
    print(x)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(price, itemno, quantity)

import numpy
x = 4
y = 6
z = x * y

name = input("Please tell ur your name: ")
print("Hi", name,"!")
