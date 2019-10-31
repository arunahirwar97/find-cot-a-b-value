from math import tan
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
x = 1/tan(a)
y = 1/tan(b)
z = ((x*y) + 1)/(x-y)
print("The value of cot(a-b) is = ",z)
