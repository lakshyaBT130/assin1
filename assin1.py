#Q.1

print("write three numbers = ")
v1 = int(input()) + int(input()) + int(input())
v2 = 3

print("avg.", int(v1)/int(v2))

#Q.2
print("Please enter you Gross Income to the nearest penny and your income should be more than $10000")
grossincome = float(input())
print("Please enter the number of dependents you have")
depandance = int(input())
income = float(grossincome - 10000 - (depandance * 3000))
print("Your taxable income is = $", income)
tax = float(20/100 * income)
print("Your income tax= $", tax)

#Q.3
SID = int(input("your SID"))
Name = input("your name")
gender = input("your gender")
Course = input("your course")
CGPA   = float(input("your CGPA"))
list = [SID, Name , gender, Course ,CGPA ]
print(list)

#Q.4
print("Enter the marks of 5 students")
marks = []
for i in range(0, 5):
    ele = int(input())
    marks.append(ele)
marks.sort()
print("marks in sorted manner", marks)

#Q.5a
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del color[3]
print ("specified list after removing 4th element ", color)

Q.5b
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = ['Purple' if (i == 'Black') | (i == 'Pink') else i for i in color]
print(color)
