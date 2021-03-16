# Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes displayed
# on the 24th digital clock.


N = int(input("Enter the minutes passed since midnight:"))
hours = (N//60)
minute = (N%60)
print("The hour is %s" %(hours))
print(f"The minute is {minute}")
for i  in range(3):
    print("The time right now is {}:{}am".format(hours, minute))