#from datetime import datetime

#This is the regular way to do it
# first_name = "Susan"
# print("Task completed")
# print(datetime.datetime.now())
# print()

# for x in range(0,10):
#     print(x)
# print("task completed")
# print(datetime.datetime.now())



#this is a better way to do it if you are going to be repeating a function.
# def print_time():
#     print("Task completed")
#     print(datetime.now())
#     print()

# first_name = "Susan"
# print_time()

# for x in range(0,10):
#     print(x)
# print_time()




#Another example where you have different messages being printed.
# first_name = "Susan"
# print("first name assigned")
# print(datetime.now())
# print()

# for x in range(0,10):
#     print(x)
# print("loop completed")
# print(datetime.now())
# print()


# def print_time(task_name):
#     print(task_name)
#     print(datetime.now())
#     print()

# first_name = "Susan"
# print_time("first name assigned")

# for x in range(0,10):
#     print(x)
# print_time("loop completed")




# Example 5

import math

# Define a function named main.
def main():
    # Get the radius and height from the user.
    radius = float(input("Enter the radius of a cylinder: "))
    height = float(input("Enter the height of a cylinder: "))

    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Print the volume of the cylinder.
    print(f"Volume: {volume:.2f}")

# Start this program by
# calling the main function.
main()