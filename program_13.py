"""angry bird dodge game"""

import pygame
import random
import time

pygame.init() # initialize all the modules that come with pygame

pygame.mixer.init(899999999) # initialize frequency to 899999999

#bird_collision = pygame.mixer.Sound("angry_bird_collosion.mp3")

#bgr_sound = pygame.mixer.Sound("main_theme.mp3")

display_width = 1350 # win width
display_height = 700 # win height

black = (0,0,0) # black color 
white = (255,255,255) # white color

red = (200,0,0) # red color
green = (0,200,0) # green color
blue = (0,0,255) # blue
brown = (165,42,42) # brown color

bright_red = (255,0,0)
bright_green = (0,255,0)
fps = 130# game speed

pause = False # flag variable

h_s = 0 # for high score

custom_color1 = (109,139,128) 

x_change = 0

bird_width = 177

game_display = pygame.display.set_mode((display_width,display_height)) # set window size

pygame.display.set_caption("Angry Bird ") # game window title

clock = pygame.time.Clock() # for fps/game clock

# loading images
angry_bird_img = pygame.image.load("angrybird3.jpg")
pig1_img = pygame.image.load("pig1.jpg")
pig2_img = pygame.image.load("pig2.png")
pig3_img = pygame.image.load("pig3.jpg")
pig4_img = pygame.image.load("pig4.jpg")
pig5_img = pygame.image.load("pig6.jpg")
pig6_img = pygame.image.load("pig7.jpg")
#bg_image = pygame.image.load("angry_bird_background_1.png")
background_img = pygame.image.load("angry_bird_background_1.png")

#bomb_img = pygame.image.load("bomb.jpg")

def things_dodged(count) :

    font = pygame.font.SysFont("comicsansms",45)
    text = font.render("Dodged : "+str(count),True,red)
    game_display.blit(text,(0,0))

def high_score() :

    global h_s

    font = pygame.font.SysFont("comicsansms",45)
    text = font.render("High SCore : "+str(h_s),True,red)
    game_display.blit(text,(0,1100))

    pygame.display.update()

    
def angry_bird_characters(x,y) :

    #game_display.blit(background_img,(0,0))# blit method is used to draw backgound stuff
    game_display.blit(angry_bird_img,(x,y))
    game_display.blit(pig1_img,(1200,475))
    game_display.blit(pig2_img,(1200,230))
    game_display.blit(pig3_img,(1200,40))
    game_display.blit(pig4_img,(-30,90))
    game_display.blit(pig6_img,(-10,290))
    game_display.blit(pig5_img,(-30,530))
     
def text_objects(text,font,color) :

     textSurface = font.render(text,True,color) # True for transparent
     return textSurface , textSurface.get_rect()

def button(msg,x,y,w,h,ac,ic,action=None) :

        # creating mouse object
        mouse = pygame.mouse.get_pos() # mouse[0] = x-pos & mouse[1] = y-pos
        # creating mouse click object
        click = pygame.mouse.get_pressed() # click[0] = lmb , click[1] = mouse wheel , click[2] = rmb        

        # if mouse position is between x-pos of rect and x-pos and width of rect
        # and mouse position is between y-pos of rect and y-pos and height of rect
        if (x+w > mouse[0] > x) and (y+h > mouse[1] > y) :

            pygame.draw.rect(game_display,ac,(x,y,w,h))

            if (click[0] == 1) and (action != None) : # if lmb is clicked

                action() # eg. button("start",350,450,100,50,green,bright_green,game_loop) . action = game_loop i.e, action() = game_loop()

        else :

            pygame.draw.rect(game_display,ic,(x,y,w,h))        

        smallText = pygame.font.SysFont("comicsansms",20)
        textSurf , textRect = text_objects(msg,smallText,white)

        textRect.center = ((x+(w/2)),(y+(h/2))) # 150 = x-pos , 100 = width , 450 = y-pos , height = 50

        game_display.blit(textSurf,textRect)      
            
  

def display_message(text,size=115) :

     largeText = pygame.font.SysFont("comicsansms",size) # to adjust font
     textSurf , textRect = text_objects(text,largeText,green) # returning 
     textRect.center = ((display_width/2,display_height/2)) # rectangle position
     game_display.blit(textSurf,textRect) # add to window
     pygame.display.update() # update window

     time.sleep(2)

     game_loop()

def quit_game() :

    pygame.quit()
    quit()
    
def unpause():
    
    global pause

    pygame.mixer.music.unpause()# un-pause music
    pause = False
    
def paused():

    global pause
    
    pygame.mixer.music.pause() # pause music
    pygame.mixer.music.load("pause_music.mp3")
    pygame.mixer.music.play(-1)

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText,red)
    TextRect.center = ((display_width/2),(display_height/2))
    game_display.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue",450,450,100,50,green,bright_green,unpause)
        button("Quit",850,450,100,50,red,bright_red,quit_game)

        pygame.display.update()
        clock.tick(15)   

def crash() :

     pygame.mixer.music.stop() # stop previous music
     pygame.mixer.music.load("angry_bird_collosion.mp3") # load crash music file
     pygame.mixer.music.play() # play the file

     largeText = pygame.font.SysFont("comicsansms",115)
     TextSurf, TextRect = text_objects("Game Over", largeText,blue)
     TextRect.center = ((display_width/2),(display_height/2))
     game_display.blit(TextSurf, TextRect)
    

     while True:
         for event in pygame.event.get():
             #print(event)
             if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
                
         #gameDisplay.fill(white)
        

         button("Play Again",450,450,100,50,green,bright_green,game_loop)
         button("Quit",850,450,100,50,red,bright_red,quit_game)

         pygame.display.update()
         clock.tick(15)

def things(thing_x,thing_y,thing_startx,thing_starty,color) : # blocks to be drawn

    pygame.draw.rect(game_display,color,[thing_x,thing_y,thing_startx,thing_starty])     
          
def game_intro() :

    intro = True # intro part true

    pygame.mixer.music.load("main_theme.mp3")
    pygame.mixer.music.play()

    while intro :

        for event in pygame.event.get() :

            if event.type == pygame.QUIT :

                pygame.quit()

        largeText = pygame.font.SysFont("comicsansms",115) # to adjust font
        textSurf , textRect = text_objects("Angry Bird Dodge",largeText,white) # returning 
        textRect.center = ((display_width/2,display_height/2)) # rectangle position
        game_display.blit(textSurf,textRect) # add to window

        # calling function
        button("start",350,450,100,50,green,bright_green,game_loop)
        button("Quit",850,450,100,50,red,bright_red,quit_game)
        
        pygame.display.update() # update window
        clock.tick(10)  
 
def game_loop() :

     global h_s
     global pause

     x = (400) # we want to display image at 'x' position

     y = (510) # we want to display image at 'y' position

     game_exit = False # for game loop

     x_change = 0

     thing_startx = random.randrange(200,1200)
     thing_starty = -600
     thing_speed = 3
     thing_width = 190
     thing_height = 100

     dodged = 0 # set dodge value

     pygame.mixer.music.stop() # stop previous music
     pygame.mixer.music.load("funky_theme.mp3")
     pygame.mixer.music.play()

     while not game_exit :

         for event in pygame.event.get() : # pygame.event.get() does the work of checking events per fps

             if event.type == pygame.QUIT :

                 pygame.quit()
                 quit()# game loop flag variable

             if event.type == pygame.KEYDOWN : # if the down arrow key is pressed 

                 if event.key == pygame.K_LEFT : # if left arrow key is pressed
                     x_change = -15

                 if event.key == pygame.K_RIGHT : # if right arrow key is pressed
                     x_change = 15

                 if event.key == pygame.K_p :
                     pause = True
                     paused()

             if event.type ==  pygame.KEYUP : # if up arrow key is pressed

                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :

                     x_change = 0 # do nothing

         x += x_change             

         game_display.fill(white) # fill screen with white color

         


         # things(thing_x,thing_y,thing_w,thing_h,color)
         things(thing_startx,thing_starty,thing_width,thing_height,brown) # create thing object
         
         thing_starty += thing_speed # for each iteration the thing moves 7-pixels down

         angry_bird_characters(x,y) # calling function

         things_dodged(dodged)

         high_score()

         # 185 is the width of the pig7 image

         if (x < 150) or (x > 1240 - bird_width) : # if bird crosses screen exit game 

              crash()   

         if  (thing_starty > display_height) : # if the thing goes off the screen

             thing_starty = 0 - thing_height # start at y-position
             thing_startx = random.randrange(200,1200) # start obj at random place on x-axis

             dodged += 1 # increase dodge value



             thing_speed += 2 # increase obj speed

         if ( y+10 < thing_starty + thing_height  ) : # if thing overlaps the bird at y-axis

             #if bird touches the object on the left side                               if bird touches the object on the right side

              # added extra 50 px because image is a bird of irregular shape    and   reducted 50 px as image is a bird of irregular shape 

             if ((x + 50 > thing_startx) and (x + 50 < thing_startx + thing_width)) or ((x + (bird_width -50) > thing_startx) and (x + (bird_width - 50) < thing_startx + thing_width)) :

                  c_s = dodged # assign dodged score to current score

                  crash()    # game over               
             
         pygame.display.update( ) # to update the window

         clock.tick(60)# for fps (to run through this loop at 60 fps speed) (or) speed of the game .

game_intro() 
game_loop()    # calling method     

pygame.quit() # quit pygame

quit() # quit python
