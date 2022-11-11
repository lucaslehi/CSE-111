import math

# def main():
#     print("This program computes the area of a rectangle")
#     rectangles = input("How many rectagles are we computing? ")
#     width = float(input("width "))
#     height = float(input("height "))
    
#     rectangle_area = compute_rectangle_area(width, height)
#     print(f"The area is {rectangle_area}")

# def compute_rectangle_area(width,height):
#     return width * height

# main()

def main():
    print("This program computes the area of a rectangle")
    quantity = number_of_rectangles()
    total_area = calculate_total_area(quantity)
    display(total_area)

def number_of_rectangles():
    number_of_rectangles = input("How many rectagles are we computing? ")

def rectagle_dimensions():
    width = float(input("width "))
    height = float(input("height "))

def compute_rectangle_area(width, height):
    return width * height
    
main()