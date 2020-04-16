from tkinter import *

# Create window object
app = Tk()
app.title('Detection of mathematical equations')

canvas_width = 600
canvas_height = 450


def paint(event):
    color = 'red'
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    c.create_oval(x1, y1, x2, y2, fill=color, outline=color)


c = Canvas(app, width=canvas_width, height=canvas_height, bg='white')
c.pack(expand=YES, fill=BOTH)
c.bind('<B1-Motion>', paint)

message = Label(app, text='Press and Drag to draw')
message.pack(side=BOTTOM)
app.mainloop()
