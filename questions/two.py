# Name and age of a person.

name = input("Enter the name:")
age = int(input("Enter the age:"))
print(name, "is the name and " + str(age) + " is the age")
print("%s is the name and %s is the age" % (name, age))
print("{} is the name and {} is the age".format(name, age))
print(f"{name} is the name and {age} is the age")