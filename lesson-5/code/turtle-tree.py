import turtle
import os
t = turtle.Turtle()
win = turtle.Screen()
t.home()
win.clear()
t.pu()
t.bk(300)
t.pd()



img = 0

def tree(length,t):
    global img
    os.system('import -window 0x1c01c2d image{0:03d}.jpg'.format(img))
    img+=1
    if length < 5:
        return None
    else:
        t.forward(length)
        t.right(50)
        tree(length-30,t)
        t.left(100)
        tree(length-30,t)
        t.right(50)
        t.backward(length)


tree(180,t)

