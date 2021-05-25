from tkinter import *
#from turtle import pos
from time import sleep, time

HEIGHT = 1000
WIDTH = 1600

window = Tk()
window.title('2D_Test')

c = Canvas(window, width=WIDTH, height=HEIGHT, bg='blue')
c.pack()

berg_move = 10

#ground
ground = c.create_rectangle(0,700,1700,1000,fill='green')

#berge
berg = c.create_polygon(0,30,150,-600,300,30,fill='gray')
c.move(berg, 1601, 670)

berg2 = c.create_polygon(0,30,150,-400,300,30,fill='gray')
c.move(berg2, 1701, 670)

berg3 = c.create_polygon(0,30,150,-500,300,30,fill='gray')
c.move(berg3, 1800, 670)

#sky
sun_id = c.create_oval(0,0,150,150, fill='yellow')
c.move(sun_id, 100, 100)

clowd_id = c.create_oval(0,0,300,150, fill='white')
c.move(clowd_id, 500, 150)

#strand
strand = c.create_polygon(0,30,1000,300,1000,30,fill='yellow')
c.move(strand, 1701, 671)

meer = c.create_polygon(200,30,1200,300,1200,30,fill='darkblue')
c.move(meer, 1701, 670)

#auto glass
auto_glas_id = c.create_rectangle(0,0,150,75, fill='blue', outline='white',width=5)
c.move(auto_glas_id, 905, 567)

#player 3
player_id3 = c.create_rectangle(5,5,50,100,fill='purple')
c.move(player_id3, 800, 600)

head_id3 = c.create_oval(0,0,50,50, fill='pink')
c.move(head_id3, 803, 555)

left_id3 = c.create_oval(0,0,5,5, fill='black')
c.move(left_id3, 820, 565)

right_id3 = c.create_oval(0,0,5,5, fill='black')
c.move(right_id3, 830, 565)

mouse_id3 = c.create_rectangle(0,0,20,1,fill='black')
c.move(mouse_id3, 818, 590)

#player1
player_id = c.create_rectangle(5,5,50,100,fill='red')
c.move(player_id, 800, 600)

head_id = c.create_oval(0,0,50,50, fill='pink')
c.move(head_id, 803, 555)

left_id = c.create_oval(0,0,5,5, fill='black')
c.move(left_id, 820, 565)

right_id = c.create_oval(0,0,5,5, fill='black')
c.move(right_id, 830, 565)

mouse_id = c.create_rectangle(0,0,20,1,fill='black')
c.move(mouse_id, 818, 590)

GESCHW = 10

#player 2
player_id2 = c.create_rectangle(5,5,50,100,fill='yellow')
c.move(player_id2, 800, 600)

head_id2 = c.create_oval(0,0,50,50, fill='pink')
c.move(head_id2, 803, 555)

left_id2 = c.create_oval(0,0,5,5, fill='black')
c.move(left_id2, 820, 565)

right_id2 = c.create_oval(0,0,5,5, fill='black')
c.move(right_id2, 830, 565)

mouse_id2 = c.create_rectangle(0,0,20,1,fill='black')
c.move(mouse_id2, 818, 590)

#auto body

auto_body_id = c.create_rectangle(0,0,300,80, fill='black')
c.move(auto_body_id, 830, 640)

auto_left = c.create_oval(0,0,50,50, fill='black')
c.move(auto_left, 870, 720)

auto_right = c.create_oval(0,0,50,50, fill='black')
c.move(auto_right, 1030, 720)

#corona = c.create_oval(0,0,1000,1000, fill='darkblue',outline='green', width=50,)
#c.move(corona, 1701, 0)

GESCHW = 10

def move_player(event):
    if event.keysym == 'w':# and pos2[3] > 700:
        Up = 10
        
        c.move(player_id2, 0, -Up)
        c.move(head_id2, 0, -Up)
        
        c.move(left_id2, 0, -Up)
        c.move(right_id2, 0, -Up)
        c.move(mouse_id2, 0, -Up)
        
    elif event.keysym == 's' and pos2[3] < 930:
        c.move(player_id2, 0, GESCHW)
        c.move(head_id2, 0, GESCHW)
        
        
        c.move(left_id2, 0, GESCHW)
        c.move(right_id2, 0, GESCHW)
        c.move(mouse_id2, 0, GESCHW)
        
    elif event.keysym == 'a':
        c.move(player_id2, -GESCHW, 0)
        c.move(head_id2, -GESCHW, 0)
        
        c.move(left_id2,  -GESCHW, 0)
        c.move(right_id2, -GESCHW, 0)
        c.move(mouse_id2, -GESCHW, 0)
                
    elif event.keysym == 'd':
        c.move(player_id2, GESCHW, 0)
        c.move(head_id2, GESCHW, 0)
        
        c.move(left_id2,  GESCHW, 0)
        c.move(right_id2, GESCHW, 0)
        c.move(mouse_id2, GESCHW, 0)

    if event.keysym == 't':# and pos2[3] > 700:
        Up = 10
        
        c.move(player_id3, 0, -Up)
        c.move(head_id3, 0, -Up)
        
        c.move(left_id3, 0, -Up)
        c.move(right_id3, 0, -Up)
        c.move(mouse_id3, 0, -Up)
        
    elif event.keysym == 'g' and pos2[3] < 930:
        c.move(player_id3, 0, GESCHW)
        c.move(head_id3, 0, GESCHW)
        
        
        c.move(left_id3, 0, GESCHW)
        c.move(right_id3, 0, GESCHW)
        c.move(mouse_id3, 0, GESCHW)
        
    elif event.keysym == 'f':
        c.move(player_id3, -GESCHW, 0)
        c.move(head_id3, -GESCHW, 0)
        
        c.move(left_id3,  -GESCHW, 0)
        c.move(right_id3, -GESCHW, 0)
        c.move(mouse_id3, -GESCHW, 0)
            
    elif event.keysym == 'h':
        c.move(player_id3, GESCHW, 0)
        c.move(head_id3, GESCHW, 0)
        
        c.move(left_id3,  GESCHW, 0)
        c.move(right_id3, GESCHW, 0)
        c.move(mouse_id3, GESCHW, 0)

    if event.keysym == 'Up':# and pos[3] > 700:
        Up = 10
        
        c.move(player_id, 0, -Up)
        c.move(head_id, 0, -Up)
        #c.move(sun_id, 0, 1)
        #c.move(clowd_id, 0, 1)
        #c.move(ground, 0, 1)
        c.move(left_id, 0, -Up)
        c.move(right_id, 0, -Up)
        c.move(mouse_id, 0, -Up)
        
    elif event.keysym == 'Down' and pos[3] < 930:
        c.move(player_id, 0, GESCHW)
        c.move(head_id, 0, GESCHW)
        #c.move(sun_id, 0, -1)
        #c.move(clowd_id, 0, -1)
        #c.move(ground, 0, -1)
        c.move(left_id, 0, GESCHW)
        c.move(right_id, 0, GESCHW)
        c.move(mouse_id, 0, GESCHW)
        
    elif event.keysym == 'Left':
        c.move(player_id, -GESCHW, 0)
        c.move(head_id, -GESCHW, 0)
        #c.move(sun_id, 1, 0)
        #c.move(clowd_id, 1, 0)
        c.move(left_id,  -GESCHW, 0)
        c.move(right_id, -GESCHW, 0)
        c.move(mouse_id, -GESCHW, 0)
            
    elif event.keysym == 'Right':
        c.move(player_id, GESCHW, 0)
        c.move(head_id, GESCHW, 0)
        #c.move(sun_id, -1, 0)
        #c.move(clowd_id, -1, 0)
        c.move(left_id,  GESCHW, 0)
        c.move(right_id, GESCHW, 0)
        c.move(mouse_id, GESCHW, 0)
    
    if event.keysym == '1':
        c.move(auto_glas_id, -GESCHW, 0)
        c.move(auto_body_id, -GESCHW, 0)
        
        c.move(auto_left,  -GESCHW, 0)
        c.move(auto_right, -GESCHW, 0)
     
    elif event.keysym == '3':
        c.move(auto_glas_id, GESCHW, 0)
        c.move(auto_body_id, GESCHW, 0)
        
        c.move(auto_left,  GESCHW, 0)
        c.move(auto_right, GESCHW, 0)

    if event.keysym == 'q':
        #berg_move =  -1
        c.move(berg, -berg_move, 0 )
        c.move(berg2, -berg_move, 0 )
        c.move(berg3, -berg_move, 0 )
    elif event.keysym == 'e':
        #berg_move = 0 
        c.move(berg,  berg_move, 0 )
        c.move(berg2,  berg_move, 0 )
        c.move(berg3,  berg_move, 0 )

    if event.keysym == 'r':
        c.move(strand, -GESCHW, 0)
        c.move(meer, -GESCHW, 0)
     
    elif event.keysym == 'y':
        c.move(strand, GESCHW, 0)
        c.move(meer, GESCHW, 0)

c.bind_all('<Key>', move_player)

while True:
    
    window.update()
    
    pos = c.coords(player_id)
    pos2 = c.coords(player_id2)

    sleep(0.01)