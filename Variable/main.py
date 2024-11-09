# Variable = A container for a value (string, integer, float, boolean)
# A variable behaves as if it was the value. it contains.

#string =" "

first_name = "Atiqur Rahman"
food = "pizza"
email = "mdatiqurrahmancse@gmail.com"

print (f"Hello {first_name}")
print(f"You like {food}")
print(f"your email is : {email}")

# Integers

age = 25
quantity = 3
num_of_student = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_student} students")

#Float

price = 10.99
gpa = 3.69
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is {gpa}")
print(f"You run {distance} km")

#Boolean

is_student = True

print(f"Are you student? : {is_student}")

is_student  = False

if is_student:
    print("you are a student")
else:
    print("you are not a student")