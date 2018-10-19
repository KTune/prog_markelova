from tkinter import *
root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

def left_click(event):
    print('left click')

def right_click(event):
    print('right click')


canv.bind('<Button-1>', left_click)
canv.bind('<Button-3>', right_click)

mainloop()