import math

item = int(input("Enter the number of items: "))
box = int(input("Enter the number of items por box: "))

need = math.ceil(item/box)

print(f"For {item} items, packing {box} in each box, you will need {need} boxes.")