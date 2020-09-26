from classes import Surf
from datetime import datetime



now=datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)



print(datetime.fromtimestamp(
        int("1284105682")
    ).strftime('%Y-%m-%d %H:%M:%S')
)


print("Hello fellow surfer babes and dudes.\n\n Let's see how gnarly the waves are today on the Gold Coast.")

#return surf height range for the day
word=Surf()

print(word.surf_report())



#return the surf height for that time of day, as well as wind


