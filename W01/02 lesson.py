#import math 

# EX 1
#print(int(input("What number?")))

#str((int(input(print("Enter a number: ")))))
#print(str(round(float(input))))
#print(type(len(list((round(math.sqrt(abs(float(str(int(input("Enter an interge: "))))),1)))))))

#EX 2
#print("Hello, I", 20 , sep=" am ", end= " how old are you", flush=True)

#EX 3
#power = (17**9)/3
#power = round(power)
#power = power - 6
#print(power)

#*Guihub co pilot 

#def random_math():
#    return (math.ceil(math.pow(17, 9) / 3) - 6) % 2 == 0
#print(random_math())

#EX 4
#import random
#random_number_list = []
#while len(random_number_list) < 100:
#    random_number_list.append (random.randint(0, 1000))
#random_number_list.sort()
#print(random_number_list)

#EX 5
from datetime import datetime

now = datetime.now()
#current_time = now.strftime("%H:%M:%S")
#print("Current Time =", current_time)
display_message = "even minute"
if (now.minute % 2 > 0):
    display_message = "odd minute"
print (display_message)

