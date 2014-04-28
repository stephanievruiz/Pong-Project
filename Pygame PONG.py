#This program allows the user to play the game PONG

import sys, os, math, random
import pygame
from pygame.locals import *



class Paddle(pygame.sprite.Sprite):
    #The paddles in the game

    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)

        #image and rect
        self.image = pygame.image.load(os.path.join('images','pong_paddle.gif'))
        self.rect = self.image.get_rect()

        #position, movement speed and velocity of paddle
        self.rect.centerx, self.rect.centery = xy
        self.movementspeed = 5
        self.velocity = 0

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
        elif self.rect.top +dy < 0
            self.rect.top = 0
        else:
            self.rect.y += dy

    def update(self):
        #updated sprite and handles moving sprite by velocity
        self.move(self.velocity)
                                                    
class Game(object):

    def __init__(self):
        #load and set up
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption ("PONG")

        #If user hits an exit key
        pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

        #background of game and line down center
        self.background = pygame.surface((800,400))
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
        self.rightpaddle = Paddle(750,200)
        self.sprites.add(self.rightpaddle)
                                                    
                            

    def run(self):
        print "Starting Event Loop"
        running = True

        #tick pygame clock, can limit fps
        while running:
            self.clock.tick()

        #If user closes game, stop running
            running = self.handleEvents()
            
        #update title and render screen
            pygame.display.set_caption("PONG %d fps" % self.clock.get_fps())
            pygame.display.flip()

        print "Quitting. Thanks for playing!"

    def handleEvents(self):
        #poll for pygame events
        for event in pygame.event.get():

           #handling user input to quit game 
            if event.type == QUIT:
                return False

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False

        return True

#Creating and Running the game
    
if __name__ == '__main__':
    game = Game()
    game.run()
        
