# Write a program that reads the length of base and height of right-angled-triangle and print the area.Every no.
# is given on seperate line.

length = int(input("Enter the length of the base:"))
height = int(input("Enter the height of the triangle:"))
area = (1/2) * length * height
for i in range(3):
    print(f"The area of the triangle is {area}")