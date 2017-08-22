import tkinter

class ball:
  def __init__(self, Canvas,  x0, y0, x1, y1, color):
    self.x0 = x0
    self.y0 = y0
    self.x1 = x1
    self.y1 = y1
    self.color = color

    self.Canvas = Canvas
    self.Ball = Canvas.create_oval(self.x0, self.y0, self.x1, self.y1, fill = self.color)

  def move(self, speedx, speedy):
    self.speedx = speedx
    self.speedy = speedy
    move(self.Ball, self.speedx, self.speedy)
    after(1000, self.move)
