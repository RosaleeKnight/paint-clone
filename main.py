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
            self.draw = ImageDraw.Draw(self.image)

            self.btn_frame = Frame(self.root)
            self.btn_frame.pack(fill=X)

            self.btn_frame.columnconfigure(0, weight=1)
            self.btn_frame.columnconfigure(1, weight=1)
            self.btn_frame.columnconfigure(2, weight=1)

            self.clear_btn = Button(self.btn_frame, text="Clear", command=self.clear)
            self.clear_btn.grad(row=0, column=1, sticky="W+E")

            self.save_btn = Button(self.btn_frame, text="Save", command=self.save)
            self.save_btn.grad(row=1, column=2, sticky="W+E")
            
            self.bplus_btn = Button(self.btn_frame, text="B+", command=self.brush_plus)
            self.bplus_btn.grad(row=0, column=0, sticky="W+E")
            
            self.bminus_btn = Button(self.btn_frame, text="B-", command=self.brush_minus)
            self.bminus_btn.grad(row=1, column=0, sticky="W+E")

            self.color_btn = Button(self.btn_frame, text="Change Color", command=self.change_color)
            self.color_btn.grad(row=1, column=1, sticky="W+E")

        def paint(self):
            pass

        def clear(self):
            pass

        def save(self):
            pass

        def brush_plus(self):
            pass

        def brush_minus(self):
            pass

        def change_color(self):
            pass