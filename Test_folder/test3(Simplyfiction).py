import random
from tkinter import *
import math


##------------------------------------------##
##-------------Global variable--------------##
##------------------------------------------##

x=random.randint(0,360)


##------------------------------------------##
## This function retrieves values from Serial ##
##------------------------------------------##
# def con():
#     global x
#     x=x+random.randint(-10,10)
#     return x

##------------------------------------------##
## Updating Earth arcs for animation ##
##------------------------------------------##
def tilt(arcnme,deg):
    deg += random.randint(-10,10)
    c.itemconfig(arcnme,start = deg) # Updates values of arcs start angle.
    root.after(100,tilt(arcnme, deg))
    print(deg)

##------------------------------------------##
## Updating Sky Arc for animation ##
##------------------------------------------##
# def tiltsky():
#
#     x= con()
#     c.itemconfig("sky",start = x+180) # Updates values of arcs start angle.
#     root.after(100,tiltsky)
#     print(x)


##------------------------------------------##
## Main geometry and setting goes here##
##------------------------------------------##
root = Tk()
root.title("Control Panel")
root.geometry('1200x750')
frame_1 = Frame(root)

frame_1.grid(row = 0,column = 0)

c = Canvas(frame_1,width = 200, height = 200, bg = 'white')

c.pack()



eartharc = c.create_arc(-100, -100, 300, 300,start = x,extent=-180, fill="red",tags="earth")
# skyarc = c.create_arc(-100, -100, 300, 300,start = x+180,extent=-180, fill="#5F9EA0",tags="sky")



tilt(arcnme="earth",deg=x)
tiltsky()
root.mainloop()