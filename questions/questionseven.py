# You live 4 miles from university. The bus drives at 25 m/h but spends 2 minutes at each of the 10 stops on the way.
# How long will the bus journey take? Alternatively, you could run to university. You jog the first mile at 7 m/h; then
# run the next two at 15 m/h; before jogging the last at 7 m/h again. Will this be quicker or slower then bus?


distance = 4 * 1.6 * 1000
speed_bus = 25 /(60 * 60)
time_taken = ((((distance/speed_bus) + (2 * 60))//60)//60)//24
print(f"The bus will take {time_taken} days to reach university")

speed_student1 = 7/(60 * 60)
time_taken1 = (1.6 * 1000)/ speed_student1
speed_student2 = 15/(60 * 60)
time_taken2 = (2 * 1.6 * 1000)/speed_student2
speed_student3 = 7/(60 * 60)
time_taken3 = (1.6 * 1000)/ speed_student3

TotalTimeTaken = time_taken1 + time_taken2 + time_taken3
TotalTimeTaken_day = (((TotalTimeTaken//60)//60)//24)
print(f"It takes {TotalTimeTaken_day}days for the boy to reach the university")

if time_taken < TotalTimeTaken_day :
    print("The boy will reach slower than bus")
else:
    print("The boy will reach faster than bus.")







