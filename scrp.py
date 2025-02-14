
import math 
import pygame as py 
  
py.init() 
  
clock = py.time.Clock() 
  
FrameHeight = 600
FrameWidth = 1200
  
# PYGAME FRAME WINDOW 
py.display.set_caption("Endless Scrolling in pygame") 
screen = py.display.set_mode((FrameWidth, 
                              FrameHeight)) 
  
# IMAGE 
bg = py.image.load(r"Race Game\images\track.bmp")
  
# DEFINING MAIN VARIABLES IN SCROLLING 
scroll = 0
  
# CHANGE THE BELOW 1 TO UPPER NUMBER IF 
# YOU GET BUFFERING OF THE IMAGE 
# HERE 1 IS THE CONSTATNT FOR REMOVING BUFFERING 
tiles = math.ceil(FrameWidth / bg.get_width()) + 1
  
# MAIN LOOP 
while 1: 
    # THIS WILL MANAGE THE SPEED OF 
    # THE SCROLLING IN PYGAME 
    clock.tick(33) 
  
    # APPENDING THE IMAGE TO THE BACK 
    # OF THE SAME IMAGE 
    i = 0
    while(i < tiles): 
        screen.blit(bg, (bg.get_width()*i 
                         + scroll, 0)) 
        i += 1
    # FRAME FOR SCROLLING 
    scroll -= 6
  
    # RESET THE SCROLL FRAME 
    if abs(scroll) > bg.get_width(): 
        scroll = 0
    # CLOSINF THE FRAME OF SCROLLING 
    for event in py.event.get(): 
        if event.type == py.QUIT: 
            quit() 
  
    py.display.update() 
  
py.quit() 
