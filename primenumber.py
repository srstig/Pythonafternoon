#Python program that checks whether a number is a prime number or not
number = int(input("Enter the number to check:"))

def is_prime(number):
    if number > 1 :
        for i in range(2,(number//2)+1):
            return False
        return True

if is_prime(number):
    print(number,"is a prime number")

else:
    print(number,"is not a prime number")