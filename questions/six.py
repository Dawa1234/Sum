# Solve each of the following problems using Pythonscripts. Make you use appropriate variables and comments.
# When there is final answer, have Python print it to the screen.
#     A person's body mass index(BMI) is defined as:
#         BMI = (mass in kg) / ( height in m)^2

mass = int(input("Enter the weight of the person:"))

height = float(input("Enter the height of the person in meter:"))

BMI = mass / (height ** 2)

print("The body mass index of the person is %s kg/m.sq." %(BMI))