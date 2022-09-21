import random
from tkinter import *
import time


##------------------------------------------##
##-------------Global variable--------------##
##------------------------------------------##

x=random.randint(0,360)
y=random.randint(0,360)


##------------------------------------------##
## This function retrieves values from Serial ##
##------------------------------------------##
def con():
    global x
    x=x+random.randint(-10,10)
    time.sleep(0.1)
    return x
##------------------------------------------##
## This function retrieves values from Serial ##
##------------------------------------------##
def cony():
    global y
    y=y+random.randint(-3,3)
    return y

##------------------------------------------##
## Creating and Updating Earth arcs for animation ##
##------------------------------------------##
def tiltearth():

    c.itemconfig("earth",start = con()) # Updates values of arcs start angle.
    c.itemconfig("sky", start=con() + 180)  # Updates values of arcs start angle.
    root.after(100, tiltearth)
    print("x=", x)




##------------------------------------------##
## Creating and Updating Sky Arc for animation ##
##------------------------------------------##
def tiltNS():

    #y= cony()
    c.itemconfig("NS",start = cony()) # Updates values of arcs start angle.
    root.after(100,tiltNS)
    print("y=",y)

##------------------------------------------##
## Creating and Updating Sky Arc for animation ##
##------------------------------------------##
def tiltWE():

    #y= cony()
    c.itemconfig("WE",start = cony()+90) # Updates values of arcs start angle.
    root.after(100,tiltWE)


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

x = 0

eartharc = c.create_arc(-100, -100, 300, 300,start = x,extent=-180,outline="#5F9EA0", fill="red",tags="earth")
NSarc = c.create_arc(-100, -100, 300, 300,start = y,extent=-180,outline="black", fill="",tags="NS")
WEarc = c.create_arc(-100, -100, 300, 300,start = y,extent=-180,outline="black", fill="",tags="WE")
skyarc = c.create_arc(-100, -100, 300, 300,start = x+180,extent=-180,outline="#5F9EA0", fill="#5F9EA0",tags="sky")




tiltearth()
tiltNS()
tiltWE()
# tiltsky()
root.mainloop()