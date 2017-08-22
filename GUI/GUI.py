import tkinter
from tkinter import *
from ball import *

root = tkinter.Tk()
root.title('Example')
canvas = tkinter.Canvas(root, width=600, height=400, bg='white')
canvas.grid(row=0, column=0)
canvas.create_line([0, 0, 600, 400], width = 2, fill = 'blue')

# ball class
canvas.create_oval(0, 0, 120, 120, fill = 'red')

ball_2 = ball(canvas, 10, 10, 30, 30, 'blue')
ball_1 = ball(canvas, 100, 100, 180, 180, 'green')


root.mainloop()

