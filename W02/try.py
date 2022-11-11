import math

width = float(input("Enter the width of the tire in mm (ex 205) : "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60) : "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15) : "))

volume = (math.pi * (width**2) * ratio) * ((width * ratio) + (2540 * diameter)) / 10000000000

volume = round(volume, 2)

print(f"The approximate volume is {volume} liters")

print()
small = str("$80-$150")
medium = str("$100-250")
large = str("$200-500")

if diameter <= 15:
    print(f"Tires that are {int(diameter)} inches, ususally cost between {small} per unit.")
elif diameter > 15 and diameter <= 20:
    print(f"Tires that are {int(diameter)} inches, ususally cost between {medium} per unit.")
else:
    print(f"Tires that are {int(diameter)} inches, ususally cost between {large} per unit.")
    
print()

buyer = input("Would you like to buy tires that have the dimensions specified above? Enter yes or no? ")


""" if buyer.lower() == "yes" or buyer.lower() == "y":
    print(input("We will have an associate call you. What is your phone number? "))
    print("We will contact you soon. Have a great day")
elif buyer.lower() == "no" or buyer.lower() == "n":
    print("Have a great day. Let us know if you change your mind")
else:
    while buyer != buyer.lower() in ["yes", "y", "no", "n"]:
        print(input("Type yes or no. "))
 """

if buyer.lower() == "yes" or buyer.lower() == "y":
    phone = input("Please, type your phone number: ")
    print()
    with open('volumes.txt', "at") as volumes_file:
        print(f"The user's phone is: {phone}", file=volumes_file)
    print(f"Thank you! One of our agents will contact you as soon as possible on this phone number - {phone}\n")
    print("Have a great day!!!\n")
else:
    print("Thank you and have a great day!!!")
    






