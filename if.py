
num1 = int(input("INTER NUMBER FIVE: "))
num2 = int(input("INTER NUMBER TEN: "))


if num1 == 5:
    print("Number 1 five*: ")
elif num1 >= 6:
    print("Number 1 greater that five*: ")
elif num1 <= 4:
    print("Number 1 less that five*: ")
if num2 == 10:
    print("Number 2 ten*: ")
elif num2 >= 11:
    print("Number 2 greare that ten*: ")
elif num2 <= 9:
    print("Number 2 less that ten*: ")
if num1 == 10 and num2 == 5:
    print("The required numbers are reversed!")
if num1 == 5 or num2 == 10:
    print("Half life or 1\\2")

YOUBOB = True #1
YOUBOR = False #0
YOUKARL = False #0

if num1 == 50 and YOUBOB:
    print("Bob alles 50!")

if num1 == 50 and YOUBOB == False:
    print("Sorry, you isn't Bob")

if num2 == 100 and not YOUKARL:
    print("Ha! Karl alles 100!")

num3 = input("Введите слово\t\"CLEVER\":")
if num3 == "CLEVER":
    print("You are clever!")
else:
    print("You are a bor)))")


num4 = "Больше чем 10 " if num1 > 10 else "Меньше чем 10 "
print(num4)

