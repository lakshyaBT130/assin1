#1
def GradeCalc(num):
    if num < 25:
        print('F')
    elif num >= 25 and num < 45:
        print('E')
    elif num >= 45 and num < 50:
        print('D')
    elif num >= 50 and num < 60:
        print('C')
    elif num >= 60 and num < 80:
        print('B')
    else:
        print('A')


a = int(input("Enter total marks= "))
GradeCalc(a)


#2
def LeapYear(num):
    if num % 4 == 0:
        if num % 100 != 0:
            print("it is a Leap year")
        elif num % 100 == 0:
            if num % 400 == 0:
                print("it is a Leap Year")
            else:
                print("not a Leap year")
    else:
        print("not a Leap year")


a = int(input("Year= "))
LeapYear(a)


#3
import random
for i in range(10):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    print(f"Question {i+1}:", end="")
    user_output = int(input(f"{num1}X{num2}="))
    if user_output == (num1*num2):
        print("Right!")
    else:
        print(f"Wrong.The right answer is {num1*num2}")



#4
x = 200

for candies in range(x):

    if candies % 5 == 2:
        if candies % 6 == 3:
            if candies % 7 == 2:
                print(candies, 'candies are in the bowl!')
                break
