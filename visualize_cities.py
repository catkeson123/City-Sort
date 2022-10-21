# Author: Calvin Atkeson
# Date: 11/8/21
# Purpose: Lab 3 visualization

from cs1lib import *
from sort_cities import *

img = load_image("world.png")
i = 0

# center of window
cx = 720 // 2
cy = 360 // 2

# drawing function
# no parameters
def main():
    global i
    draw_image(img, 0, 0)

    # draw each city
    for n in range(i):
        x = cx + cities[n].longitude * 2
        y = cy - cities[n].latitude * 2
        set_fill_color(1, 0, 0)
        draw_rectangle(int(x), int(y), 3, 3)


    # increment i to draw 50 cities
    if i < 50:
        i = i + 1

start_graphics(main, width = 720, height = 360, framerate = 5)
