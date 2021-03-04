# N students take k apples and distributes them among each others evenly. The remaining (the undivisible) part
# reamains in the basket. How many apples will each single student get? How many apples will remain in the basket?

apple = int(input("Enter the no. of apple: "))
student = int(input("Enter the no. of students: "))
each_students = apple//student
remaining = apple%student
print(f"Each student gets {each_students} apple")
print("The remaining apple in the basket is", remaining)