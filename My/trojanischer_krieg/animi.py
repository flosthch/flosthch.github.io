from tkinter import *
from PIL import Image

HEIGHT = 1000
WIDTH = 1600
GESCHW = 10

window = Tk()
window.title('DER TROJANISCHE KRIEG')

c = Canvas(window, width=WIDTH, height=HEIGHT, bg='blue')
c.pack()

berg_move = 10

#personen 
#schiff 
imgschiff = PhotoImage(file="./schiff.png")
schiff = c.create_image(0,0, anchor=NW, image=imgschiff)
c.move(schiff, 160, 400)

#pferd
imgPferd = PhotoImage(file="./trojanisches-pferd.png")
pferd = c.create_image(0,0, anchor=NW, image=imgPferd)
c.move(pferd, 1600, 400)

#soldaten pferd
imgsoldaten_pferd = PhotoImage(file="./Soldat_tres.png")
soldaten_pferd = c.create_image(0,0, anchor=NW, image=imgsoldaten_pferd)
c.move(soldaten_pferd, 1600, 400)

#paris 
imgparis = PhotoImage(file="./paris.png")
paris = c.create_image(0,0, anchor=NW, image=imgparis)
c.move(paris, 160, 400)

#melelaus
imgm = PhotoImage(file="./menelaus.png")
m = c.create_image(0,0, anchor=NW, image=imgm)
c.move(m, 1600, 400)


#hektor


#achilles


#goetter
imggoetter = PhotoImage(file="./goetter.png")
goetter = c.create_image(0,0, anchor=NW, image=imggoetter)

#(weitere Haupfiguren)



#szene
#troja
troja = c.create_rectangle(0,800,1610,1000,fill='yellow')

#meer blue
meer = c.create_rectangle(1600,800,3200,1000,fill='darkblue')

#mauer gray
mauer = c.create_rectangle(300,300,550,800,fill='gray')
mauerSeite = c.create_rectangle(0,500,300,800,fill='gray')

#griechenland green
griechenland = c.create_rectangle(3200,800,4900,1000,fill='green')


#steuerung befehl
def round(id, left,right,up, down, event):
    if event.keysym == str(up):
        c.move(id, 0, -GESCHW)
        
    elif event.keysym == down:
        c.move(id, 0, GESCHW)
        
        
    elif event.keysym == left:
        c.move(id, -GESCHW, 0)
        
            
    elif event.keysym == right:
        c.move(id, GESCHW, 0)

def line(id, left, right, event):
    if event.keysym == left:
        c.move(id, -GESCHW, 0)
        
            
    elif event.keysym == right:
        c.move(id, GESCHW, 0)

def move(event):
    #line(pferd,1,2,event) #pferd
    #round(soldaten_pferd,"a","d","w","s",event) #soldat pferd
    
    #pferd
    id = pferd
    left = "1"
    right = "2"
    if event.keysym == left:
        c.move(id, -GESCHW, 0)
        
            
    elif event.keysym == right:
        c.move(id, GESCHW, 0)
    
    #soldat pferd
    id = soldaten_pferd
    left = "a"
    right = "d"
    up = "w"
    down = "s"
    if event.keysym == str(up):
        c.move(id, 0, -GESCHW)
        
    elif event.keysym == down:
        c.move(id, 0, GESCHW)
        
        
    elif event.keysym == left:
        c.move(id, -GESCHW, 0)
        
            
    elif event.keysym == right:
        c.move(id, GESCHW, 0)

    id = [troja,meer,mauer,mauerSeite,griechenland]
    left = "3"
    right = "4"
    for i in range(len(id)):
        if event.keysym == left:
            c.move(id[i], -GESCHW, 0)
            
                
        elif event.keysym == right:
            c.move(id[i], GESCHW, 0)

    id = goetter
    left = "f"
    right = "h"
    up = "t"
    down = "g"
    if event.keysym == str(up):
        c.move(id, 0, -GESCHW)
        
    elif event.keysym == down:
        c.move(id, 0, GESCHW)
        
        
    elif event.keysym == left:
        c.move(id, -GESCHW, 0)
        
            
    elif event.keysym == right:
        c.move(id, GESCHW, 0)

    id = schiff
    left = "5"
    right = "6"
    if event.keysym == left:
        c.move(id, -GESCHW, 0)
        
            
    elif event.keysym == right:
        c.move(id, GESCHW, 0)

    id = m
    left = "k"
    right = ";"
    up = "o"
    down = "l"
    if event.keysym == str(up):
        c.move(id, 0, -GESCHW)
        
    elif event.keysym == down:
        c.move(id, 0, GESCHW)
        
        
    elif event.keysym == left:
        c.move(id, -GESCHW, 0)
        
            
    elif event.keysym == right:
        c.move(id, GESCHW, 0)

    id = paris
    left = "y"
    right = "i"
    up = "7"
    down = "u"
    if event.keysym == str(up):
        c.move(id, 0, -GESCHW)
        
    elif event.keysym == down:
        c.move(id, 0, GESCHW)
        
        
    elif event.keysym == left:
        c.move(id, -GESCHW, 0)
        
            
    elif event.keysym == right:
        c.move(id, GESCHW, 0)

c.bind_all('<Key>', move)


while True:
    
    window.update()

