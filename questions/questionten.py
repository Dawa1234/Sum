# Write a python program to convert seconds to day, hour , minutes and seconds.

time = int(input("Enter the time in sec: "))
minutes = time / 60
hours = minutes / 60
day = hours / 24
print(f"{minutes} minutes.")
print(f"{hours} hours.")
print(f"{day} day.")