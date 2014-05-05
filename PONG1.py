#This program allows the user to play the game PONG

import sys, os, math, random
import pygame
from pygame.locals import *

## i hope this works

class Ball(pygame.sprite.Sprite):

    def __init__(self,xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('pong_ball.png'))
        self.rect = self.image.get_rect()

        self.rect.centerx, self.rect.centery = xy
        self.maxspeed = 10
        self.servespeed = 5
        self.velx = 0
        self.vely = 0    
        
    def reset(self):
        self.rect.centerx, self.rect.centery = 400,200
        self.velx = 0
        self.vely = 0
        
    def serveBall(self):
        angle = random.randint(-60,60)

        if abs(angle) < 5 or abs(angle-180) < 5:
            angle = random.randint(10,20)

        if random.random() > .5:
            angle += 180
            
        x = math.cos(math.radians(angle))
        y = math.sin(math.radians(angle))

        self.velx = self.servespeed * x
        self.vely = self.servespeed * y
        
        


class Paddle(pygame.sprite.Sprite):
    #The paddles in the game

    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)

        #image and rect
        self.image = pygame.image.load(os.path.join('pong_paddle.png'))
        self.rect = self.image.get_rect()

        #position, movement speed and velocity of paddle
        self.rect.centerx, self.rect.centery = xy
        self.movementspeed = 5
        self.velocity = 0
        self.score = 0,0

    def up(self):
        #increases vertical velocity
        self.velocity -= self.movementspeed

    def down(self):
        #Decreases vertical velocity
        self.velocity += self.movementspeed
    
    def move(self, dy):
        #Moving paddle in y direction
        if self.rect.bottom + dy > 400:
            self.rect.bottom = 400
        elif self.rect.top +dy < 0:
            self.rect.top = 0
        else:
            self.rect.y += dy

    def update(self):
        #updated sprite and handles moving sprite by velocity
        self.move(self.velocity)


        
class GameScore(pygame.sprite.Sprite):

    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.xy = xy
        self.font = pygame.font.Font(None, 50)

        #Displaying score at top of screen
        self.leftscore = 0
        self.rightscore = 0
        self.reRender()

    #Adds points to player (left or right)
    def left(self):
        self.leftscore +=1
        self.reRender()
        
    def right(self):
        self.rightscore += 1
        self.reRender()

    #resetting and updating scores
    def reset(self):
        self.leftscore = 0
        self.rightscore = 0
        self.reRender()

    def reRender(self):
        self.image = self.font.render("%d    %d"%(self.leftscore, self.rightscore),True, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = self.xy
        
class Game(object):

    def __init__(self):
        #load and set up
        pygame.init()
        
        self.window = pygame.display.set_mode((800, 400))
        
        self.clock = pygame.time.Clock()
        
        pygame.display.set_caption("PONG")

        #If user hits an exit key
        pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

        #background of game and line down center
        self.background = pygame.Surface((800,400))
        self.background.fill((0,0,0))
        pygame.draw.line(self.background, (255,255,255), (400,0), (400,400), 2)
        self.window.blit(self.background, (0,0))

        #flip display so background is on
        pygame.display.flip()

        #Sprite rendering group for ball and paddles
        self.sprites = pygame.sprite.RenderUpdates()

        #Creating paddles and adding to sprite group
        self.leftpaddle = Paddle((50,200))
        self.sprites.add(self.leftpaddle)
        self.rightpaddle = Paddle((750,200))
        self.sprites.add(self.rightpaddle)
        
        self.ball = Ball((400,200))
        self.sprites.add(self.ball)

        self.scoreImage = GameScore((400,100))
        self.sprites.add(self.scoreImage)

        pygame.mixer.init()
        pygame.mixer.music.load('musicA.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1.0)
           
                
                                                    
                            

    def run(self):
        print ("Starting Event Loop")
        
        running = True

        #tick pygame clock, can limit fps
        while running:
            
            self.clock.tick(60)

            #If user closes game, stop running
            running = self.handleEvents()

             #update title and render screen
            pygame.display.set_caption("PONG %d fps" % self.clock.get_fps())

            self.manageBall()
            #updates the sprites
            for sprite in self.sprites:
                sprite.update()
            #renders sprites
            self.sprites.clear(self.window, self.background)
            dirty = self.sprites.draw(self.window)

            #blits dirty areas of the screen?
            pygame.display.update(dirty)
            
        print ("Quitting. Thanks for playing!")

    def handleEvents(self):
        #poll for pygame events
        for event in pygame.event.get():
           #handling user input to quit game 
            if event.type == QUIT:
                print("Quitting. Thanks for playing!")
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
                
                

            elif event.type == KEYDOWN:
                
                if event.key == K_ESCAPE:
                    print("Quitting. Thanks for playing!")
                    pygame.quit()
                    sys.exit()
                    

                if event.key == K_w:
                    self.leftpaddle.up()
                if event.key == K_s:
                    self.leftpaddle.down()
                    
                if event.key == K_UP:
                    self.rightpaddle.up()
                if event.key == K_DOWN:
                    self.rightpaddle.down()

                if event.key == K_SPACE:
                    if self.ball.velx == 0 and self.ball.vely ==0:
                        self.ball.serveBall()
               
                    
            elif event.type == KEYUP:
                if event.key == K_w:
                    self.leftpaddle.down()
                if event.key == K_s:
                    self.leftpaddle.up()

                if event.key == K_UP:
                    self.rightpaddle.down()
                if event.key == K_DOWN:
                    self.rightpaddle.up()

                    
        return True


    def manageBall(self):
        self.ball.rect.x += self.ball.velx
        self.ball.rect.y += self.ball.vely

        if self.ball.rect.top < 0:
            self.ball.rect.top = 1

            self.ball.vely *= -1

        elif self.ball.rect.bottom > 400:
            self.ball.rect.bottom = 399

            self.ball.vely *= -1

        if self.ball.rect.left < 0:
            self.scoreImage.left()

            self.ball.reset()
            return
        
        elif self.ball.rect.right > 800:
            self.scoreImage.right()
            
            self.ball.reset()
            return

        collided = pygame.sprite.spritecollide(self.ball, [self.leftpaddle, self.rightpaddle], dokill = False)

        if len(collided) > 0:
            hitpaddle = collided[0]

            self.ball.velx *= -1
            self.ball.rect.x += self.ball.velx
            
##    def manageAiPaddle(self):
##        if self.ball.vely == self.aileftpaddle.rect.centery:
##            pass
##        elif self.ball.vely > self.aileftpaddle.rect.centery:
##            self.aileftpaddle.up()
##        elif self.ball.vely < self.aileftpaddle.rect.centery:
##            self.aileftpaddle.down()
            
            
           
if __name__ == '__main__':
    game = Game()
    game.run()
        
