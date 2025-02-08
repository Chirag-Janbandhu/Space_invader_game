import pygame
import random
import math
from pygame import mixer

#intitialize pygame
pygame.init()

#creating a screen
screen=pygame.display.set_mode((800,600))

#title and icons
pygame.display.set_caption("Space invaders")
icon_of_game= pygame.image.load('enemy.png')
pygame.display.set_icon(icon_of_game)

#adding player
player_img=pygame.image.load('1702089.png')
#adding the villian

#adding a background
bg_img=pygame.image.load('background.png')
#adding bullet
bullet_img=pygame.image.load('bullet.png')

#adding bacground sound
mixer.music.load('background.wav')
mixer.music.play(-1)


#resizing the image and the villian
resized_player_image=pygame.transform.scale(player_img,(64,64))

#adding img location
playerx=370
playery=480
playerx_change=0

#adding villian location
villan_img=[]
resized_villian_image=[]
villanx=[]
villany=[]
villianx_change=[]
villiany_change=[]
num_of_enemies=4
for i in range(num_of_enemies):
    villan_img.append(pygame.image.load('enemy.png'))
    resized_villian_image.append(pygame.transform.scale(villan_img[i],(64,64)))
    villanx.append(random.randint(0,735))
    villany.append(random.randint(50,150))
    villianx_change.append(2)
    villiany_change.append(40)

#adding bullet
bulletx=0
bullety=480
bulletx_change=0
bullety_change=5
bullet_status="ready"


#creating func to add the image
def player(x,y):
    screen.blit(resized_player_image,(x,y))
    
def villian(xv,yv,i):
    screen.blit(resized_villian_image[i],(xv,yv))
    
def fire_bullet(x,y):
    global bullet_status
    bullet_status="fire"
    screen.blit(bullet_img,(x+16,y+10))
    
def isCollision(bull,bullety,villanx,villany):
    distance=math.sqrt((math.pow(bull-villanx,2))+(math.pow(villany-bullety,2)))
    if distance<27:
        return True
    else:
        return False
   
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
def scoreText(x,y):
    score=font.render("Score :"+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
    
textX=10
textY=10 
bull=0

over_font= pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
   over_text=over_font.render("GAME OVER",True,(255,255,255))
   screen.blit(over_text,(200,250))

#so that computer dosent hang


running=True
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(bg_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_status is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bull = playerx
                    fire_bullet(bull, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
     
         
        
                
    
    playerx=playerx+playerx_change 
    
    #adding boundary
    if playerx<0:
        playerx=0
    elif playerx>=736:
        playerx=730
    
    for i in range(num_of_enemies): 
        
        #gameover 
        if villany[i]>440:
            for j in range(num_of_enemies):
                villany[j]=2000
            game_over_text()
            break
        
           
        villanx[i]=villanx[i]+villianx_change[i]
        if villanx[i]<0:             
            villianx_change[i]=2
            villany[i]+=villiany_change[i]
        if villanx[i]>=736:
            villianx_change[i]=-2
            villany[i]+=villiany_change[i]
            
        col=isCollision(bull,bullety,villanx[i],villany[i])
        if col==True:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bullety=480
            bullet_status="ready"
            score_value+=1
            villanx[i]=random.randint(0,735)
            villany[i]=random.randint(50,150) 
            
        villian(villanx[i],villany[i],i)   
        
    if bullety<=0:
        bullety=480
        bullet_status="ready"
    if bullet_status is "fire":
        fire_bullet(bull,bullety)
        
        bullety-=bullety_change
        
    
           
    #calling the function
    player(playerx,playery)
    scoreText(textX,textY)
    
    
    #make sure the screen gets updated every time
    pygame.display.update()
