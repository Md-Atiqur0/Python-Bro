# Type casting = The process of converting a variable from one data type to another
# str(), int(), float(), bool()

name = "Atiqur Rahman"
age = 25
gpa = 3.69
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa= int(gpa)
age = str (age)
age += "1"

print(f"{age}")