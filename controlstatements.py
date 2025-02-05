#A python program that checks for room temperature

temperature = 23
if temperature > 25 :
    print("It is too hot")
else:
    print("It is too cold")

#A program that returns the largest number
first = 67
second = 45
third = 56

if first > second and first > third :
    print(first, "is the largest number")

elif second > first and second > third:
    print(second, "is the largest number")

else:
    print(third, "is the largest number")

#Program to check a number and return whether the number is even or odd
num = 9
if num == 0:
    print(num, "is a neutral number")

elif num%2 ==0 :
    print(num, "is even")
else  :
    print(num, "is odd")