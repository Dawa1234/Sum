# Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes displayed
# on the 24th digital clock.


N = int(input("Enter the minutes passed since midnight:"))
hours = (N//60)
minute = (N%60)
print("The hour is %s" %(hours))
print(f"The minute is {minute}")
if N < 720 :
    print("The time right now is {}:{}am".format(hours, minute))

elif N == 720 :
    print("The time right now is {}:{}pm".format(hours, minute))

else:
    print("The time right now is {}:{}pm".format(hours, minute))









