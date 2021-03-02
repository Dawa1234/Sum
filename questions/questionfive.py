# A school decided to replace desk in three classroom.Each desks sits two students.Given the no. of students
# in each class,print the smallest possible numbers of desk that can be purchased.

student1 = int(input("Enter the no. of students in first class:"))
student2 = int(input("Enter the no. of students in second class:"))
student3 = int(input("Enter the no. of students in third class:"))


NumberOfDesk = student1//2
Number_OfDesk = student2//2
Number_Of_Desk = student3//2


print(f"{NumberOfDesk} desks are needed for a first class.")
print("{} desks are needed for a second class.".format(Number_OfDesk))
print("%s desks are needed for a third class." %(Number_Of_Desk))


