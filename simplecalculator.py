#Python program for simple calculator


def add(num1,num2):
    print(num1 + num2)

def subtract(num1,num2):
    print(num1-num2)

def multiply(num1,num2):
    print(num1*num2)

def divide(num1,num2):
    print(num1/num2)

print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = int(input("Enter choice(1/2/3/4):"))

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

if choice == 1:
    print(add(num1,num2))

elif choice == 2:
    print(subtract(num1,num2))

elif choice == 3 :
    print(multiply(num1,num2))

elif choice == 4:
    print(divide(num1,num2))

else:
    print("Invalid input")