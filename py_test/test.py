from tkinter import *

HEIGHT = 1000
WIDTH = 1600

window = Tk()
window.title('2D_Test')

c = Canvas(window, width=WIDTH, height=HEIGHT, bg='blue')
c.pack()

while True:
    
    window.update()