print("Simple Calculator for daily life")
print('Write 1 to add')
print('Write 2 to subtract')
print('Write 3 to multiply')
print('Write 4 to divide')

choice =   int(input("Please Select Your Operation"))
num1   =   int(input("Enter The First Number"))
num2   =   int(input("Enter The Second Number"))

addedNumber = float(num1 + num2)
subtractedNumber =float(num1 - num2)
multipliedNumber = float(num1 * num2)
dividedNumber = float(num1 / num2)

if choice == 1:
    print("Your Answer =",addedNumber)
elif choice == 2:
    print("Your Answer =",subtractedNumber)
elif choice == 3:
    print("Your Answer =",multipliedNumber)
elif choice == 4:
    print("Your Answer =",dividedNumber)
else:
    print("The Operation is invalid")    