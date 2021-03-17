#How many apples through the basket were distributed to how many persons and remained in the basket.Calculated.

apple_inbasket = int(input("Enter the no. of apple:"))
total_people = int(input("Enter the no. of people:"))
people_gotten = int(input("Enter the no. of apple distributed:"))
remaining_apple = apple_inbasket - people_gotten
total_people_got = people_gotten/total_people
#Applying Condition for apple.
if remaining_apple < 1 : print ("The is no remaining apple in the basket")
elif remaining_apple <= 1 :print("The remaining apple in the basket is", remaining_apple)
else : print("The remaining apples in the basket are", remaining_apple)
#Applying Condition for people.
if total_people_got <1 : print ("{} apple was distributed to each person.".format(total_people_got))
elif total_people_got <= 1:print("%s apples was distributed to each person."%(total_people_got))
else : print(" {} apples were distributed to each person.".format(total_people_got))