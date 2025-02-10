# 1. A simple program to check whether a year is a leap year or not
year = 2005
if year %4 ==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")


#2. A python program that checks whether a letter is a vowel or a consonant
letter = "z"

if letter.lower() in ('a', 'e', 'i', 'o', 'u'):

  print("Vowel")

elif letter.upper() in ('A', 'E', 'I', 'O', 'U'):

  print("Vowel")

else:

  print("Consonant")