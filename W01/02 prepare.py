#name = input("Please enter your name: ")
#print(f"Hello {name}")

#n = float(input("Please enter a number: "))
#r = round(n, 2)
#print(r)

#x = "sun"
#y = "moon"
#z = "stars"
#print(x, y, z, sep="|", flush=True)

import math

number = float(input("Enter a number: "))
print( math.sqrt(number))
if math.sqrt(number) < 100:
    print(f"The square root is less than 100.")
elif math.sqrt(number) > 100:
    print(f"The Square root is more than 100.")
else:
    print(f"The square root is exactly 100.")