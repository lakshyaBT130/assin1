#q1
def decToBinary(a):
    if a >= 1:
        decToBinary(a//2)
    print(a % 2, end='')


num = int(input("enter number= "))
decToBinary(num)

# q2 calculator function
def calculator(int1, int2, op):
    if op == '*':
        print(int1*int2)
    if op == '/':
        print(int1/int2)
    if op == '-':
        print(int1-int2)
    if op == '+':
        print(int1+int2)
    if op == '%':
        print(int1 % int2)
    if op == '//':
        print(int1//int2)


num1 = int(input("enter num1= "))
num2 = int(input("enter num2= "))
a = input('enter operator= ')
calculator(num1, num2, a)

#q3
import math

print(int(3 + 4) * 5)
n = int(input("Enter Value of n:"))
print(n * (n - 1) / 2)
r = int(input("Enter value of r:"))
print(4 * 3.14 * r ** 2)
a = int(input("Eter value of a:"))
b = int(input("Enter value of b:"))
print(((r * (math.cos(a) ** 2)) + (r * (math.sin(b) ** 2))) ** 0.5)
y2 = int(input("Eter value of y2:"))
y1 = int(input("Enter value of y1:"))
x2 = int(input("Eter value of x1:"))
x1 = int(input("Enter value of x2:"))
print((y2 - y1) / (x2 - x1))


#q4
x = range(5)
for n in x:
    print(n)
print('\n')
y = range(3, 10)
for i in y:
    print(i)
print('\n')
z = range(4, 13, 3)
for n in z:
    print(n)
print('\n')
a = range(15, 5, -2)
for n in a:
    print(n)
print('\n')
b = range(5, 3)
for n in b:
    print(n)


#q5
from ctypes.wintypes import HACCEL


H = 1.00794
C = 12.01070
O = 15.99940


def MolWeight(a, b, c):
    print(a*H+b*C+c*O)


int1 = float(input("number of H atoms= "))
int2 = float(input("number of C atoms= "))
int3 = float(input("number of O atoms= "))
MolWeight(int1, int2, int3)
