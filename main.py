from tkinter import *
from PIL import Image, ImageDraw
import PIL

WIDTH, HEIGHT = 500, 500
CENTER = WIDTH // 2
WHITE = (255, 255, 255)


class PaintGUI:

        def __init__(self):

            self.root = TK()
            self.root.title("Paint Clone")

            self.brush_width = 15
            self.current_colour = "#000000"

            self.cnv = Canvas(self.root, width=WIDTH-10, height=HEIGHT-10, bg="white")
            self.cnv.pack()
            self.cnv.bind("<B1-Motion>", self.paint)

            self.image = PIL.Image.new("RGB", (WIDTH, HEIGHT), WHITE)
            self.draw = ImageDraw(self.image)

            

        def paint(self):
            pass