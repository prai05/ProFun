import tkinter
from tkinter import *

main = Tk()
main.title('Steelseries')


window = tkinter.Canvas(main, width = 1280, height = 720, bg = 'white')
window.grid(row = 0, column = 0)

#outside = window.create_oval(440, 160, 840, 560, fill = 'white')
#outside2 = window.create_oval(400, 120, 880, 600, fill = 'black')

inside = window.create_oval(500, 220, 780, 500, fill = 'black')
inside2 = window.create_oval(540, 260, 740, 460, fill = 'white')

lineTop = window.create_line(400,120, 880, 120)
lineBot = window.create_line(400,600, 880, 600)

lineLside = window.create_line(400, 120, 400, 600)
lineRside = window.create_line(880, 120, 880, 600)








main.mainloop()
