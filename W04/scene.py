# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="navyblue")   
    draw_stars(canvas, scene_height, scene_width)     
    draw_cloud(canvas, scene_width, scene_height)
    draw_moon(canvas)

def draw_cloud(canvas, scene_height, scene_width):       
    draw_oval(canvas, 260, 240, 50, 350, width=0, fill="lavenderblush1")   
    draw_oval(canvas, 400, 240, 200, 350, width=0, fill="lavenderblush1")
    draw_oval(canvas, 600, 240, 350, 350, width=0, fill="lavenderblush1")
    draw_oval(canvas, 150, 290, 450, 420, width=0, fill="lavenderblush1")    
    draw_oval(canvas, 500, 450, 790, 550, width=0, fill="lavenderblush1")    
    draw_oval(canvas, 400, 450, 600, 550, width=0, fill="lavenderblush1") 
    draw_oval(canvas, 550, 450, 700, 550, width=0, fill="lavenderblush1") 
        
    return

def draw_stars (canvas, scene_height, scene_width):
    min_diam = 2
    max_diam = 3
    for i in range(500):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, scene_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="gold1")
    
    return

def draw_moon(canvas):    
    draw_oval(canvas, 300, 250, 50, 500, width=0, fill="khaki2")
    
    return

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="springgreen4")
    
    #Tree 1 
    tree_center_x = 215
    tree_bottom = 30
    tree_height = 420
    draw_tree(canvas, tree_center_x, tree_bottom, tree_height)

    #Tree 2
    tree_center_x = 555
    tree_bottom = 30
    tree_height = 420
    draw_tree(canvas, tree_center_x, tree_bottom, tree_height)

    #Tree 3
    tree_center_x = 760
    tree_bottom = 30
    tree_height = 420
    draw_tree(canvas, tree_center_x, tree_bottom, tree_height)
    
    return

def draw_tree(canvas, center_x, bottom, height):
    
    # Draw a tree.
    draw_rectangle(canvas, 300, 70, 320, 120, fill="brown")
    draw_polygon(canvas, 240, 110, 310, 320, 380, 110,
            fill="forestGreen")

    # Draw another tree.
    draw_rectangle(canvas, 200, 60, 220, 110, fill="brown")
    draw_polygon(canvas, 140, 100, 210, 310, 280, 100,
            fill="forestGreen")

    # Draw a third tree.
    draw_rectangle(canvas, 100, 50, 120, 100, fill="brown")
    draw_polygon(canvas, 40, 90, 110, 300, 180, 90,
            fill="forestGreen")
    
    return

# Call the main function so that
# this program will start executing.
main()