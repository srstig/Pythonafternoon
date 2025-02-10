# built-in functions/standard library functions

y = max( 45, 89, 76, 90,458,)
print(y,"is the maximum value")

x = min(12, 4, 67 ,89, 76, 36,98,66)
print(x)

#user-defined functions
def school():
    print("emobilis")

school()

def add():
    num1 = 5
    num2 = 3
    print(num1 + num2)

add()

#/parameter/variable and argument/value
def multiply(a, b):
    print(a * b)

multiply( 5 , 8)
multiply( 12 , 8)
multiply( 78 , 4)


def employee(name, age, gender, salary, position):
    print(name, age, gender, salary, position)

employee("Maureen",25, "Female", 560000, "CEO")
employee("John",29, "Male", 450000, "HR")
employee("Ray",23, "Male", 1560000, "Managing Director")
employee("Kai",56, "Female", 560000, "CEO")
employee("Gabriela",61, "Female", 640000, "Secretary")
employee("William",55, "Male", 370000, "Assistant HR")
employee("Thomas",47, "Male", 500000, "Cleaner")
employee("Martin",38, "Male", 420000, "Teacher")
employee("Ethan",38, "Male", 590000, "Teacher")
employee("Myles",19, "Female", 30000, "Teacher")
employee("Lewis",46, "Male", 70000, "Teacher")


#A program to display details of 5 patients
def patients(fullname, gender, age, disease):
    print(fullname,gender,age,disease)

patients("Michael Rice","Male",19,"Malaria")
patients("Arya Park","Female",65,"Cancer")
patients("Natasha Moraa","Female",27,"Flu")
patients("Mohammed Hamudi","Male",36,"Measles")
patients("Terrence White","Male",8,"Typhoid")


